import json
import time
import requests
from typing import Any
from http.cookies import SimpleCookie
from urllib.parse import quote, unquote, parse_qs
from followee_notifier.types import Follower


NAME = 'twitter'
FEATURES = {
    'blue_business_profile_image_shape_enabled': True,
    'responsive_web_graphql_exclude_directive_enabled': True,
    'verified_phone_label_enabled': False,
    'responsive_web_graphql_timeline_navigation_enabled': True,
    'responsive_web_graphql_skip_user_profile_image_extensions_enabled': False,
    'tweetypie_unmention_optimization_enabled': True,
    'vibe_api_enabled': True,
    'responsive_web_edit_tweet_api_enabled': True,
    'graphql_is_translatable_rweb_tweet_is_translatable_enabled': True,
    'view_counts_everywhere_api_enabled': True,
    'longform_notetweets_consumption_enabled': True,
    'tweet_awards_web_tipping_enabled': False,
    'freedom_of_speech_not_reach_fetch_enabled': True,
    'standardized_nudges_misinfo': True,
    'tweet_with_visibility_results_prefer_gql_limited_actions_policy_enabled': False,
    'interactive_text_enabled': True,
    'responsive_web_text_conversations_enabled': False,
    'longform_notetweets_rich_text_read_enabled': True,
    'responsive_web_enhance_cards_enabled': False,
}
GRAPHQL_JSON_SEPARATOR = (',', ':')
REQUEST_INTERVAL = 3


def parse_cookies(cookies_str: str) -> dict[str, str]:
    cookies = SimpleCookie()
    cookies.load(cookies_str)
    cookies = {key: morsel.value for key, morsel in cookies.items()}
    for key in ['ct0', 'dnt', 'twid']:
        if key in cookies.keys():
            del cookies[key]
    return cookies


def graphql_url(url: str, params: dict[str, Any]) -> str:
    url += '?'
    for key, value in params.items():
        url += f'{key}={quote(json.dumps(value, separators=GRAPHQL_JSON_SEPARATOR))}&'
    if url[-1] == '&':
        url = url[:-1]
    return url


def fetch(config: dict[str, Any]) -> list[Follower]:
    result = []
    cookies = parse_cookies(config['cookies'])
    session = requests.Session()
    session.cookies.update(cookies)

    # Requset #1 - Get CSRF Token
    url = f'https://twitter.com/{config["username"]}/followers'
    print('[HTTP] >', 'GET', url)
    res = session.get(url)
    print('[HTTP] <', res.status_code)
    referer = res.url
    csrf_token = res.cookies['ct0']
    twitter_id = parse_qs(unquote(res.cookies['twid']))['u'][0]
    print(f'[DATA] Twitter ID: {twitter_id}, CSRF Token: {csrf_token}')

    # Request #2 - Get Followers
    next_cursor = None
    while True:
        graphql_variables = {"userId": str(twitter_id), "count":20, "includePromotedContent": False}
        if next_cursor:
            graphql_variables['cursor'] = next_cursor
        url = graphql_url('https://twitter.com/i/api/graphql/djdTXDIk2qhd4OStqlUFeQ/Followers', {
            'variables': graphql_variables,
            'features': FEATURES,
        })
        print('[HTTP] >', 'GET', url)
        res = session.get(url, headers={
            'referer': referer,
            'x-csrf-token': csrf_token,
            'authorization': f'Bearer {config["auth"]}',
        })
        print('[HTTP] <', res.status_code)
        if res.status_code == 429:
            rate_limit_reset = res.headers['x-rate-limit-reset']
            next_cursor = next_cursor
            sleep_time = int(rate_limit_reset) - int(time.time())
            print('[RATE LIMIT]', f'Wait for {sleep_time} seconds.')
            time.sleep(sleep_time)
            continue
        assert res.status_code == 200
        instructions = res.json()['data']['user']['result']['timeline']['timeline']['instructions']
        followers = list(filter(lambda x: x['type'] == 'TimelineAddEntries', instructions))[0]['entries']
        next_cursor = list(filter(lambda x: (x['content']['entryType'] == 'TimelineTimelineCursor') and (x['content'].get('cursorType') == 'Bottom'), followers))[0]
        followers = list(filter(lambda x: (x['content']['entryType'] == 'TimelineTimelineItem'), followers))
        followers = list(filter(lambda x: x['content'].get('itemContent', {}).get("itemType") == "TimelineUser", followers))
        followers = [i['content']['itemContent']['user_results']['result'] for i in followers]
        followers = [{
            'id': i['rest_id'],
            'url': f'https://twitter.com/i/user/{i["rest_id"]}',
            'name': i['legacy']['screen_name'],
            'display_name': i['legacy']['name'],
            'avatar': i['legacy'].get('profile_image_url_https', 'data:,'),
            'description': i['legacy'].get('description', ''),
        } for i in followers]
        result += followers
        print(f'[DATA] Fetched {len(followers)} followers, total fatched {len(result)} followers.')
        next_cursor = next_cursor['content']['value']
        print(f'[DATA] Next cursor: {next_cursor}')
        if next_cursor.startswith('0|'):
            print('[DATA] No more followers. Stop fetching.')
            break
        time.sleep(REQUEST_INTERVAL)
    return result
