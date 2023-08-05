import toml
import argparse
import datetime
import traceback
import followee_notifier.db as db
import followee_notifier.notify.smtp as smtp
import followee_notifier.notify.telegram as telegram
import followee_notifier.platforms.fake as fake
import followee_notifier.platforms.twitter as twitter
import followee_notifier.platforms.bilibili as bilibili

platforms = {
    # 'fake': fake,
    'twitter': twitter,
    'bilibili': bilibili,
}

notifiers = {
    'smtp': smtp,
    'telegram': telegram,
}

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--config', type=str, default='config.toml')
    args = parser.parse_args()
    config = toml.load(args.config)
    # config['fake'] = { 'time': 3 }

    for platform in platforms.keys():
        if config.get(platform) is None:
            print(f'[SCHEDULER] Skip {platform} because it is not configured.')
            continue
        print(f'[SCHEDULER] {platform} fetch started.')
        try:
            result = platforms[platform].fetch(config[platform])
        except Exception as _:
            print(f'[SCHEDULER] {platform} fetch failed.')
            traceback.print_exc()
            continue
        print(f'[SCHEDULER] {platform} fetch finished.')
        current_time = datetime.datetime.utcnow()
        increments = db.commit(config['sqlite'], platform, int(current_time.timestamp()), result)
        for notifier in notifiers.keys():
            if config.get(notifier) is None:
                print(f'[SCHEDULER] Skip {platform} -> {notifier} because it is not configured.')
                continue
            print(f'[SCHEDULER] {platform} -> {notifier} notify started.')
            try:
                notifiers[notifier].notify(config[notifier], platform, current_time, increments)
            except Exception as _:
                print(f'[SCHEDULER] {platform} -> {notifier} notify failed.')
                traceback.print_exc()
                continue
            print(f'[SCHEDULER] {platform} -> {notifier} notify finished.')
        print(f'[SCHEDULER] {platform} -> * finished.')
    print('[SCHEDULER] All finished.')
