import time
import requests
from typing import Any
from followee_notifier.types import Follower

NAME = 'bilibili'
REQUEST_INTERVAL = 3
REQUEST_412_WAIT = 20

def fetch(config: dict[str, Any]) -> list[Follower]:
    result = []
    base_url = f'https://api.bilibili.com/x/relation/fans?vmid={config["uid"]}&ps=20&order=desc&order_type=attention'
    page = 1
    while True:
        url = f'{base_url}&pn={page}'
        print('[HTTP] >', 'GET', url)
        res = requests.get(url, headers={ "cookie": config["cookies"] })
        print('[HTTP] <', res.status_code)
        if res.status_code == 412:
            print('[RATE LIMIT]', f'Wait for {REQUEST_412_WAIT} seconds.')
            time.sleep(REQUEST_412_WAIT)
            continue
        assert res.status_code == 200
        followers = res.json()['data']['list']
        if len(followers) == 0:
            print('[DATA] No more followers. Stop fetching.')
            break
        followers = [{
            'id': i['mid'],
            'url': f'https://space.bilibili.com/{i["mid"]}',
            'name': i['uname'],
            'display_name': i['uname'],
            'avatar': i['face'],
            'description': i.get('sign', ''),
        } for i in followers]
        result += followers
        print(f'[DATA] Fetched {len(followers)} followers, total fatched {len(result)} followers.')
        time.sleep(REQUEST_INTERVAL)
        page += 1
    return result
