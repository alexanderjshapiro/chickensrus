import base64

from app import chickensrus
from app.forms import *
from app.models import User, db, query_user, query_listing, Listing
from flask import render_template, escape, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required


@chickensrus.route('/')
def home():
    return render_template('home.html')


@chickensrus.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUp()

    error = None
    if form.validate_on_submit():
        user = query_user([form.username.data, form.email.data])
        if user is not None:
            error = 'Account already exists.'
        else:
            user = User()
            user.username = form.username.data
            user.email = form.email.data
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(request.args.get("next") or url_for('home'))

    return render_template('signup.html', form=form, error=error)


@chickensrus.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignIn()

    error = None
    if form.validate_on_submit():
        user = query_user([form.username.data])
        if user is not None and user.password_matches(form.password.data):
            login_user(user)
            return redirect(request.args.get("next") or url_for('home'))
        else:
            error = 'Incorrect username or password.'

    return render_template('signin.html', form=form, error=error)


@chickensrus.route('/signout')
def signout():
    logout_user()

    return redirect(url_for('home'))


@chickensrus.route('/account')
@login_required
def account():
    return render_template('account.html')


@chickensrus.route('/account/delete', methods=['GET', 'POST'])
@login_required
def deleteaccount():
    form = DeleteAccount()

    if form.is_submitted() and form.confirm_deletion.data is True:
        User.query.filter(User.username == current_user.username).delete()
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('deleteaccount.html', form=form)


@chickensrus.route('/listing/<int:listing_id>')
def listing(listing_id):
    listing = query_listing(escape(listing_id))
    image = base64.b64encode(listing.picture).decode('ascii')
    return render_template('listing.html', listing=listing, image=image)


@chickensrus.route('/listing/post', methods=['GET', 'POST'])
def postListing():
    form = PostListing()

    if form.validate_on_submit():
        listing = Listing()
        listing.listing_name = form.listingTitle.data
        listing.listing_description = form.listingDescription.data
        listing.price = form.listingPrice.data
        listing.picture = request.files[form.listingPicture.name].read()
        db.session.add(listing)
        db.session.commit()
        return redirect(url_for('account'))
    return render_template('postlisting.html', form=form)


@chickensrus.route('/cart')
def cart():
    return render_template('cart.html')


@chickensrus.route('/checkout')
def checkout():
    return render_template('checkout.html')
