from . import app
from flask import render_template, redirect, url_for

@app.route('/')
@app.route('/signin')
def signin():
    """ Signing in using Google Auth """
    return render_template("signin.html")

@app.route('/dashboard')
def dashboard():
    """ Dashboard to View Profiles """
    return render_template("base.html")
