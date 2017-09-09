from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    image_url = db.Column(db.String(50), nullable=False, unique=True)
    slack_username = db.Column(db.String(50), nullable=False, unique=True)
    profile = db.relationship('Profile', backref='user', lazy='dynamic')

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    interesting_things = db.Column(db.String(500), nullable=False)
    hobbies = db.Column(db.String(500), nullable=False)
