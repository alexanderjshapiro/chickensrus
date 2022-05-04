from sqlalchemy.dialects.postgresql import JSONB

from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

savedPosts = db.Table('savedPosts', db.Model.metadata, db.Column('user_id', db.Integer, db.ForeignKey('user.id')), db.Column('listing_id', db.Integer, db.ForeignKey('listing.id')))


user_cart = db.Table('user_cart',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('listing_id', db.Integer, db.ForeignKey('listing.id'))
)
    

savedPosts = db.Table('savedPosts', db.Model.metadata, db.Column('user_id', db.Integer, db.ForeignKey('user.id')), db.Column('listing_id', db.Integer, db.ForeignKey('listing.id')))



class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(254), unique=True)
    password_hash = db.Column(db.String(256))
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow)
    listings = db.relationship("Listing", secondary=savedPosts)
    picture = db.Column(db.BLOB)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    cart = db.relationship('Cart', secondary=user_cart)



    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def password_matches(self, password):
        return check_password_hash(self.password_hash, password)
        
    def __repr__(self):
        return f'<User: {self.username} {self.email}>'


class Listing(db.Model):
    __tablename__ = 'listing'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    listing_name = db.Column(db.String(128))
    listing_description = db.Column(db.String())
    price = db.Column(db.Float())
    date_posted = db.Column(db.Date(), default=datetime.utcnow, index=True)
    picture = db.Column(db.Text())

    def __repr__(self):
        return '<Listing %s>' % self.listing_name


class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(254))
    address = db.Column(db.String(95))
    city = db.Column(db.String(35))
    country = db.Column(db.String(90))
    zipcode = db.Column(db.String(11))
    card_number = db.Column(db.String(19))
    card_exp = db.Column(db.String(10))
    card_cvv = db.Column(db.String(3))
    def __repr__(self):
        return '<Order %s>' % self.id



@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def search_users(query):
    user_query_results = []
    user_query_results += User.query.filter(
        (User.username.contains(query))
    )
    return user_query_results


def search_listings(query):
    listing_query_results = []
    listing_query_results += Listing.query.filter(
        (query == Listing.id) |
        (Listing.listing_name.contains(query)) |
        (Listing.listing_description.contains(query))
    )
    return listing_query_results


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


def query_listing(listing_id):
    listing = Listing.query.get(listing_id)
    return listing
