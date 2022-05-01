from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from os import urandom
from os.path import abspath, dirname, join, exists

baseDirectory = abspath(dirname(__file__))

chickensrus = Flask(__name__)

chickensrus.config.from_mapping(
    SECRET_KEY=urandom(32),
    SQLALCHEMY_DATABASE_URI='sqlite:///' + join(baseDirectory, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(chickensrus)

login = LoginManager(chickensrus)
login.login_view = 'account_login'

from app import routes, models

if not exists('app.db'):
    db.create_all()
