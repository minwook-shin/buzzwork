import requests

from setting import BOT_TOKEN


def set_user_dm(user, text):
    url = 'https://slack.com/api/chat.postMessage?token=' + BOT_TOKEN
    print(url)
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    payload = {'channel': str(user),
               'text': text}

    r = requests.get(url=url, params=payload, headers=headers)
    print(r.url)
    return r.json()
