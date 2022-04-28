from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(254), unique=True)
    password_hash = db.Column(db.String(256))
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow, index=True)
    listings = db.relationship("Listing", backref='user', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def password_matches(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User: {self.username} {self.email}>'


class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def query_user(fields):
    user = None
    for field in fields:
        user = User.query.filter(
            (User.username == field) |
            (User.email == field)
        ).first()
        if user is not None:
            return user
    return user
