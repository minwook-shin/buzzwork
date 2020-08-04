import requests

from cache import cache
from setting import BOT_TOKEN


def get_user_list():
    url = 'https://slack.com/api/users.list?token=' + BOT_TOKEN
    all_user_list = requests.get(url).json()["members"]
    return [user for user in all_user_list if 'email' in user["profile"]]


def set_user_status(user, text, emoji):
    url = 'https://slack.com/api/users.profile.set?token=' + BOT_TOKEN
    print(url)
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    payload = {'user': str(user),
               'profile': {
                   "status_text": text,
                   "status_emoji": emoji,
                   "status_expiration": 0
               }.__str__()
               }

    r = requests.get(url=url, params=payload, headers=headers)
    print(r.url)
    return r.json()


@cache.cached(timeout=120)
def search_user(user_query):
    return_user = None
    for user in get_user_list():
        if user_query == user['profile']['email']:
            return_user = user
    if return_user is None:
        return_user = "not found"
    return return_user
