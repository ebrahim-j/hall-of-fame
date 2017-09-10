import os
import requests
import logging

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
            logging.info("User is bot")
    logging.info("User not found")


def get_user_image(px, email):
    user_obj = get_user_object(email)
    if user_obj:
        return user_obj['profile']['image_{}'.format(px)]
    return "Image null"


def get_user_handle(email):
    user_obj = get_user_object(email)
    if user_obj:
        return user_obj['name']
    return "User Handle null"

def get_first_name(email):
    user_obj = get_user_object(email)
    if user_obj:
        return user_obj['profile'].get('first_name', '')
    return "First Name null"

def get_last_name(email):
    user_obj = get_user_object(email)
    if user_obj:
        return user_obj['profile'].get('last_name', '')
    return "Last Name null"

# print(get_user_object('annette.odhiambo@andela.com'))
# print(get_user_image(24, 'annette.odhiambo@andela.com'))
# print(get_user_handle('annette.odhiambo@andela.com'))
# print(get_first_name('annette.odhiambo@andela.com'))
# print(get_last_name('annette.odhiambo@andela.com'))
