from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from app import google_api

from app.models import  User, Profile
import fetch_from_slack
import logging

from app import app, db

migrate = Migrate(app, db)
manager = Manager(app)

@manager.command
def initdb():
    db.create_all()
    print("DB initialised")

@manager.command
def dropdb():
    db.drop_all()
    print("DB dropped")

@manager.command
def populate():
    user = []
    for i, email in enumerate(google_api.get_emails()):
        user.append(fetch_from_slack.get_first_name(email))
        user.append(fetch_from_slack.get_last_name(email))
        user.append(fetch_from_slack.get_user_image(32, email))
        user.append(fetch_from_slack.get_user_handle(email))
        try:
            db.session.add(User(firstname=user[0], lastname=user[1], email=email, image_url=user[2], slack_username=user[3]))
            db.session.commit()
            db.session.add(Profile(interesting_things=google_api.get_interests()[i], email=email, hobbies=google_api.get_hobbies()[i]))
            db.session.commit()
        except:
            logging.info("Data invalid")
        user = []
    print("DB populated")

if __name__ == '__main__':
    manager.run()
