from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    image_url = db.Column(db.String, nullable=False)
    slack_username = db.Column(db.String(50), nullable=False)

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    interesting_things = db.Column(db.String, nullable=False)
    hobbies = db.Column(db.String, nullable=False)
