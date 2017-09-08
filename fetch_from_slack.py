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

# print(get_user_object('_ @ _ .com'))
# print(get_user_image(24, '_ @ _ .com'))
# print(get_user_handle('_ @ _ .com'))
