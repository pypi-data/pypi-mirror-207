import json
import sqlite3
from typing import Any

from followee_notifier.types import STANDARD_FOLLOWER_FIELDS, Follower, FollowerIncrements, StandardFollower


def parse_followers(timestamp: int, followers: list[Follower]) -> list[StandardFollower]:
    data = []
    for follower in followers:
        record = {}
        extensions = {}
        for key, value in follower.items():
            if key in STANDARD_FOLLOWER_FIELDS:
                record[key] = value
            else:
                extensions[key] = value
        record['extensions'] = json.dumps(extensions)
        record['followed'] = True
        record['last_updated'] = timestamp
        data.append(record)
    return data


def create_table(conn: sqlite3.Connection, platform: str):
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS {platform} (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            url TEXT NOT NULL,
            display_name TEXT NOT NULL,
            avatar TEXT,
            description TEXT,
            extensions TEXT,
            followed BOOLEAN NOT NULL,
            last_updated TIMESTAMP NOT NULL
        );
    """)
    conn.execute(f"""
        CREATE TABLE IF NOT EXISTS _increments (
            id INTEGER PRIMARY KEY,
            platform TEXT NOT NULL,
            last_updated TIMESTAMP NOT NULL,
            data_old TEXT NOT NULL,
            data_new TEXT NOT NULL,
            data_add TEXT NOT NULL,
            data_del TEXT NOT NULL
        );
    """)
    conn.commit()


def query_followers(conn: sqlite3.Connection, platform: str) -> list[StandardFollower]:
    cursor = conn.cursor()
    cursor.row_factory = sqlite3.Row
    cursor.execute(f"""
        SELECT * FROM {platform} WHERE followed = TRUE;
    """)
    followers = [dict(row) for row in cursor.fetchall()]
    conn.commit()
    return followers


def write_followers(conn: sqlite3.Connection, platform: str, followers: list[StandardFollower]):
    conn.execute(f"""
        UPDATE {platform} SET followed = FALSE;
    """)
    conn.commit()
    print(f'[DB] Insert {len(followers)} followers into table {platform}.')
    conn.executemany(f"""
        INSERT OR REPLACE INTO {platform}
            (id, name, url, display_name, avatar, description, extensions, followed, last_updated)
        VALUES
            (:id, :name, :url, :display_name, :avatar, :description, :extensions, :followed, :last_updated);
    """, followers)
    conn.commit()


def compute_increments(old: list[StandardFollower], new: list[StandardFollower]) -> FollowerIncrements:
    old_ids = set([follower['id'] for follower in old])
    new_ids = set([follower['id'] for follower in new])
    increments = { 'add': [], 'del': [] }
    for new_id in new_ids:
        if new_id not in old_ids:
            increments['add'].append(list(filter(lambda follower: follower['id'] == new_id, new))[0].copy())
    for old_id in old_ids:
        if old_id not in new_ids:
            increments['del'].append(list(filter(lambda follower: follower['id'] == old_id, old))[0].copy())
    increments['old'] = old.copy()
    increments['new'] = new.copy()
    return increments


def write_increments(conn: sqlite3.Connection, platform: str, timestamp: int, increments: FollowerIncrements):
    conn.execute(f"""
        INSERT INTO _increments
            (platform, last_updated, data_old, data_new, data_add, data_del)
        VALUES
            (:platform, :last_updated, :old, :new, :add, :del);
    """, {
        'platform': platform,
        'last_updated': timestamp,
        'old': json.dumps(increments['old']),
        'new': json.dumps(increments['new']),
        'add': json.dumps(increments['add']),
        'del': json.dumps(increments['del'])
    })
    conn.commit()


def commit(config: dict[str, Any], platform: str, timestamp: int, followers: list[Follower]) -> FollowerIncrements:
    conn = sqlite3.connect(config['file'])
    create_table(conn, platform)

    new_followers = parse_followers(timestamp, followers)
    old_followers = query_followers(conn, platform)
    increments = compute_increments(old_followers, new_followers)

    print(f'[COMPUTE] Followers count: old: {len(old_followers)}, new: {len(new_followers)}, add: {len(increments["add"])}, del: {len(increments["del"])}')
    
    write_followers(conn, platform, new_followers)
    write_increments(conn, platform, timestamp, increments)
    return increments
