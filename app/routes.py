import base64

from app import chickensrus
from app.forms import *
from app.models import *
from flask import render_template, escape, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required


@chickensrus.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@chickensrus.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form['query']
    results = search_listings(query)
    return render_template('search.html', results=results)


@chickensrus.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    image = base64.b64encode(current_user.picture).decode('ascii') if current_user.picture else None
    return render_template('account/account.html', current_user=current_user, image=image)


@chickensrus.route('/account/create', methods=['GET', 'POST'])
def account_create():
    form = AccountCreate()

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

    return render_template('account/account_create.html', form=form, error=error)


@chickensrus.route('/login', methods=['GET', 'POST'])
def account_login():
    form = AccountLogin()

    error = None
    if form.validate_on_submit():
        user = query_user([form.username.data])
        if user is not None and user.password_matches(form.password.data):
            login_user(user)
            return redirect(request.args.get("next") or url_for('home'))
        else:
            error = 'Incorrect username or password.'

    return render_template('account/account_login.html', form=form, error=error)


@chickensrus.route('/account/logout', methods=['GET', 'POST'])
@login_required
def account_logout():
    logout_user()
    return redirect(url_for('home'))


@chickensrus.route('/account/edit', methods=['GET', 'POST'])
@login_required
def account_edit():
    form = AccountEdit(
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        username=current_user.username,
        email=current_user.email
    )

    error = None
    if form.validate_on_submit():
        if current_user.password_matches(form.password.data):
            current_user.picture = request.files[form.picture.name].read()
            current_user.first_name = form.first_name.data
            current_user.last_name = form.last_name.data
            current_user.username = form.username.data
            current_user.email = form.email.data
            if form.new_password.data:
                current_user.set_password(form.new_password.data)
            db.session.add(current_user)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            error = 'Incorrect password.'

    return render_template('account/account_edit.html', form=form, error=error)


@chickensrus.route('/account/delete', methods=['GET', 'POST'])
@login_required
def account_delete():
    form = AccountDelete()

    if form.is_submitted() and form.confirm_deletion.data is True:
        db.session.delete(current_user)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('account/account_delete.html', form=form)


@chickensrus.route('/listing/<int:listing_id>', methods=['GET', 'POST'])
def listing(listing_id):
    listing = query_listing(escape(listing_id))
    image = base64.b64encode(listing.picture).decode('ascii')
    form = SaveListing()

    if form.validate_on_submit():
        current_user.listings.append(listing)
        db.session.add(current_user)
        db.session.commit()
        flash("Listing Saved")

    return render_template('listing.html', listing=listing, image=image, form=form)


@chickensrus.route('/listing/post', methods=['GET', 'POST'])
@login_required
def postListing():
    form = PostListing()

    if form.validate_on_submit():
        thisListing = Listing()
        thisListing.listing_name = form.listingTitle.data
        thisListing.listing_description = form.listingDescription.data
        thisListing.price = form.listingPrice.data
        thisListing.picture = request.files[form.listingPicture.name].read()
        db.session.add(thisListing)
        db.session.commit()
        return redirect(url_for('listing', listing_id=thisListing.id))
    return render_template('postlisting.html', form=form)


@chickensrus.route('/cart', methods=['GET', 'POST'])
def cart():
    return render_template('cart.html')


@chickensrus.route('/checkout', methods=['GET', 'POST'])
def checkout():
    form = Checkout()

    if form.validate_on_submit():
        order = Checkout()
        order.first_name = form.first_name.data
        order.last_name = form.last_name.data
        order.email = form.email.data
        order.address = form.address.data
        order.city = form.city.data
        order.country = form.country.data
        order.zipcode = form.zipcode.data
        order.card_number = form.card_number.data
        order.card_exp = form.card_exp.data
        order.cart_cvv = form.card_cvv.data
        db.session.add(order)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('checkout.html', form=form)

