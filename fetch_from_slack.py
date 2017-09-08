import os
import requests

# Fetch user objects based on their emails
req = requests.get(
    'https://slack.com/api/users.list?token={}'.format(
        os.getenv('SLACK_TOKEN')))

# List of users objects
members = req.json()['members']


def get_user_object(email):
    for user in members:
        try:
            if email == user.get('profile').get('email'):
                return user
        except KeyError:
            print("User is bot")
    print("User not found")


def get_user_image(px, email):
    user_obj = get_user_object(email)
    return user_obj['profile']['image_{}'.format(px)]


def get_user_handle(email):
    user_obj = get_user_object(email)
    return user_obj['name']

def get_first_name(email):
    user_obj = get_user_object(email)
    return user_obj['profile']['first_name']

def get_last_name(email):
    user_obj = get_user_object(email)
    return user_obj['profile']['last_name']


print(get_user_object('annette.odhiambo@andela.com'))
print(get_user_image(24, 'annette.odhiambo@andela.com'))
print(get_user_handle('annette.odhiambo@andela.com'))
print(get_first_name('annette.odhiambo@andela.com'))
print(get_last_name('annette.odhiambo@andela.com'))
