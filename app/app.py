from flask import Flask, url_for, redirect, session, render_template
from authlib.integrations.flask_client import OAuth

@app.route("/")
def hello():
    email = dict(session).get('email', None)
    return render_template('index.html')

@app.route('/login')
def login():
    google =oauth.create_client('google')
    redirect_uri = url_for('authorize', _external=True)
    return google.authorize_redirect(redirect_uri)

@app.route('/authorize')
def authorize():
    google = oauth.create_client('google')
    token = google.authorize_access_token()
    resp = google.get('userinfo')
    resp.raise_for_status()
    user_info = resp.json()
    # do something with the token and profile
    session['email'] = user_info['email']
    return render_template('support.html')