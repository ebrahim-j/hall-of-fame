from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


app = Flask(__name__, instance_relative_config=True)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://haytnqoguvwksg:fede5a6dbcd48641272864554e89292af2b447391867ff5e89ed7c876caed0ac@ec2-54-163-233-201.compute-1.amazonaws.com:5432/d37ce1hm77dq9i'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///hof'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


db = SQLAlchemy(app)

migrate = Migrate(app, db)

from . import views

