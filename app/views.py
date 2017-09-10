from flask import render_template, redirect, url_for
from . import app

@app.route('/')
@app.route('/signin')
def signin():
    """ Signing in using Google Auth """
    return render_template("sign_in.html")

@app.route('/dashboard')
def dashboard():
    """ Dashboard to View Profiles """
    return render_template("base.html")
