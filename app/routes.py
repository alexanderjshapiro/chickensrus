from app import chickensrus
from flask import render_template, escape


@chickensrus.route('/')
@chickensrus.route('/index')
@chickensrus.route('/home')
@chickensrus.route('/default')
def home():
    return render_template('home.html')


@chickensrus.route('/login')
def login():
    return render_template('login.html')


@chickensrus.route('/account')
def account():
    return render_template('account.html')


@chickensrus.route('/listing/<int:listingID>')
def listing(listingID):
    return render_template('listing.html', listingID=escape(listingID))


@chickensrus.route('/cart')
def cart():
    return render_template('cart.html')


@chickensrus.route('/checkout')
def checkout():
    return render_template('checkout.html')
