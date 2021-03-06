import sys

from app import db, login
from datetime import datetime
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

# Association tables
user_listing = db.Table(
    'user_listing',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('listing_id', db.Integer, db.ForeignKey('listing.id'))
)

user_wishlist = db.Table(
    'user_saved_for_later',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('listing_id', db.Integer, db.ForeignKey('listing.id'))
)

user_cart = db.Table(
    'user_cart',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('listing_id', db.Integer, db.ForeignKey('listing.id'))
)

user_orders = db.Table(
    'user_orders',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('order_id', db.Integer, db.ForeignKey('order.id'))
)

order_listings = db.Table(
    'order_listings',
    db.Column('order_id', db.Integer, db.ForeignKey('order.id')),
    db.Column('listing_id', db.Integer, db.ForeignKey('listing.id'))
)


# User table and helper functions
class User(UserMixin, db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), unique=True)
    email = db.Column(db.String(254), unique=True)
    password_hash = db.Column(db.String(256))
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow)
    picture = db.Column(db.String())
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    user_listings = db.relationship('Listing', secondary=user_listing, backref='user')
    user_wishlist = db.relationship('Listing', secondary=user_wishlist)
    user_cart = db.relationship('Listing', secondary=user_cart)
    user_orders = db.relationship('Order', secondary=user_orders, backref='user')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def password_matches(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return f'<User: {self.username} {self.email}>'


@login.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


def search_users(query):
    user_query_results = []
    user_query_results += User.query.filter(
        (User.username.contains(query))
    )
    return user_query_results


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


# Listing table and helper functions
class Listing(db.Model):
    __tablename__ = 'listing'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    order_id = db.Column(db.Integer, db.ForeignKey('order.id'))
    name = db.Column(db.String(128))
    description = db.Column(db.String())
    price = db.Column(db.Float())
    date_posted = db.Column(db.Date(), default=datetime.utcnow, index=True)
    picture = db.Column(db.String())

    def __repr__(self):
        return f'<Listing: {self.id} {self.name}>'


def query_listing(listing_id):
    listing = Listing.query.get(listing_id)
    return listing


def sort_date(element):
    return element.date_posted


def sort_price(element):
    return element.price


def sort_name(element):
    return element.name


def search_listings(query, results_filter=None, results_sort=None):
    listing_query_results = []
    listing_query_results += Listing.query.filter(
        ((query == Listing.id) | (Listing.name.contains(query)) | (Listing.description.contains(query))) &
        (
            (Listing.price >= results_filter['price_min']) &
            (Listing.price <= results_filter['price_max']) &
            (Listing.date_posted >= results_filter['date_min']) &
            (Listing.date_posted <= results_filter['date_max'])
        )
    )

    if results_sort == 'date_descending':
        listing_query_results.sort(key=sort_date, reverse=True)
    elif results_sort == 'date_ascending':
        listing_query_results.sort(key=sort_date)
    elif results_sort == 'price_ascending':
        listing_query_results.sort(key=sort_price)
    elif results_sort == 'price_descending':
        listing_query_results.sort(key=sort_price, reverse=True)
    elif results_sort == 'name_descending':
        listing_query_results.sort(key=sort_name)
    elif results_sort == 'name_ascending':
        listing_query_results.sort(key=sort_name, reverse=True)
    else:
        listing_query_results.sort(key=sort_date)

    # wallahi i'm finished
    return listing_query_results


# Order table and helper functions
class Order(db.Model):
    __tablename__ = 'order'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_listings = db.relationship('Listing', secondary=order_listings, backref='listing')
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    email = db.Column(db.String(254))
    address = db.Column(db.String(95))
    city = db.Column(db.String(35))
    country = db.Column(db.String(90))
    zip_code = db.Column(db.String(11))
    card_number = db.Column(db.String(19))
    card_exp = db.Column(db.String(10))
    card_cvv = db.Column(db.String(3))

    def __repr__(self):
        return '<Order %s>' % self.id  # Displays order id


def query_order(order_id):
    order = Order.query.get(order_id)
    return order
