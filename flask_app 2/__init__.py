from flask import Flask, render_template, request
from yelpapi import YelpAPI
import requests
import json
from flask_talisman import Talisman

# 3rd-party packages
from flask import Flask, render_template, request, redirect, url_for
from flask_mongoengine import MongoEngine
from flask_login import (
    LoginManager,
    current_user,
    login_user,
    logout_user,
    login_required,
)
from flask_bcrypt import Bcrypt
from werkzeug.utils import secure_filename

# stdlib
import os
from datetime import datetime

# local
app = Flask(__name__)
app.config["MONGODB_HOST"] = "mongodb://localhost:27017/final3"
app.config["SECRET_KEY"] = b"L\x9d\xfcY\xf1`\x91\xeb\\\xba\xf9\xb5\x8a'\x9c\x1f"

app.config.update(
    SESSION_COOKIE_HTTPONLY=True,
    SESSION_COOKIE_SAMESITE="Lax",
)

csp = {
    'default-src': "'self'",
    'img-src': ['*', "data:"],
    'style-src': ["'self'",'api.yelp.com/v3/businesses/search']
}

tal = Talisman(app, content_security_policy=csp, force_https=False, content_security_policy_nonce_in=['script-src'])

db = MongoEngine(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"
bcrypt = Bcrypt(app)

api_key = "-hRiWcErZsV9imRBP6C_fukk1OrTfZ0aWuK2fjLsv4tLYQCBAWXlIKN6WTocuY2PjLXXyq4g0F4ASuDWdv82VJidAAl35qvygXhmxmzOW-9nSIE1hT6oVQDVzaVRZHYx"
yelp_api = YelpAPI(api_key)