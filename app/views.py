from flask import render_template, redirect, url_for
from . import app
from .models import User, Profile

@app.route('/')
@app.route('/signin')
def signin():
    """ Signing in using Google Auth """
    return render_template("sign_in.html")

@app.route('/dashboard')
def dashboard():
    """ Dashboard to View Profiles """
    andelans = User.query.all()
    profiles = Profile.query.all()
    return render_template("base.html", andelans=andelans, profiles=profiles)

@app.route('/dashboard/<email_address>')
def profile(email_address):
	""" View a Specific User Profile """
	andelans = User.query.all()
	profiles = Profile.query.all()
	andelan = User.query.filter_by(email=email_address).first()
	profile = Profile.query.filter_by(email=email_address).first()
	return render_template("profile.html",
		andelan=andelan, profile=profile,
		andelans=andelans, profiles=profiles)
    return render_template("base.html")
