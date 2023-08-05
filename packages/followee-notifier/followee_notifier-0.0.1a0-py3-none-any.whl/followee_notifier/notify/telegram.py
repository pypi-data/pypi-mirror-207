import toml
import requests
import argparse
from datetime import datetime
from typing import Any
from followee_notifier.types import FollowerIncrements


def send_message(token: str, chat_id: int, text: str) -> dict:
    url = f'https://api.telegram.org/bot{token}/sendMessage'
    print(f'[HTTP] >', 'POST', f'https://api.telegram.org/bot********/sendMessage')
    print(f'[HTTP] >', {'chat_id': chat_id, 'parse_mode': 'HTML'})
    data = {'chat_id': chat_id, 'text': text, 'parse_mode': 'HTML'}
    response = requests.post(url, data=data)
    print(f'[HTTP] <', response.status_code)
    return response.json()


def list_chats():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, default='config.toml')
    args = parser.parse_args()
    config = toml.load(args.config)
    token = config['telegram']['token']
    url = f'https://api.telegram.org/bot{token}/getUpdates'
    updates = requests.get(url).json()['result']
    chat_ids = []
    chat_names = []
    for update in updates:
        message = update.get('message') or update.get('edited_message') or update.get('channel_post') or update.get('edited_channel_post')
        if message is None:
            continue
        chat = message.get('chat')
        if chat is None:
            continue
        chat_id = chat.get('id')
        if chat_id is None:
            continue
        if chat_id in chat_ids:
            continue
        chat_ids.append(chat_id)
        chat_name = chat.get('title') or chat.get('first_name') or chat.get('username')
        chat_names.append(chat_name)
    chat_id_max = max(len(str(i)) for i in chat_ids) + 2
    chat_name_max = max(len(i) for i in chat_names) + 2
    chat_name_max = min(chat_name_max, 80 - chat_id_max)
    print(f'{"Chat ID":<{chat_id_max}}  {"Chat Name":<{chat_name_max}}')
    print(f'{"-" * chat_id_max}  {"-" * chat_name_max}')
    for chat_id, chat_name in zip(chat_ids, chat_names):
        print(f'{chat_id:<{chat_id_max}}  {chat_name}')


"""
Telegram message formats
------------------------
<b>bold</b>
<i>italic</i>
<u>underline</u>
<code>code</code>
<a href="https://www.example.com/">link</a>
"""

def notify(config: dict[str, Any], platform: str, fetched_at: datetime, increments: FollowerIncrements):
    formatted_time = fetched_at.strftime('%Y-%m-%d %H:%M:%S UTC')
    message = f'<b>Follower information for <code>{platform}</code> as of <code>{formatted_time}</code></b>\n'
    old_count = len(increments['old'])
    new_count = len(increments['new'])
    add_count = len(increments['add'])
    del_count = len(increments['del'])
    message += f"<b>Count</b>: {len(increments['old'])} -> {len(increments['new'])}\n\n"
    if (old_count == 0):
        message += f'No followers before.\n'
    else:
        if (old_count == new_count):
            message += f'No new followers.\n'
        if (add_count > 0):
            message += f'<b>New followers</b>: {new_count}\n'
            for follower in increments['add']:
                message += f'{follower["display_name"]} (<a href="{follower["url"]}">{follower["name"]}</a>) - <code>{follower["id"]}</code>\n'
        if (del_count > 0):
            message += f'<b>Lost followers</b>: {del_count}\n'
            for follower in increments['del']:
                message += f'{follower["display_name"]} (<a href="{follower["url"]}">{follower["name"]}</a>) - <code>{follower["id"]}</code>\n'
    send_message(config['token'], config['chat'], message)
