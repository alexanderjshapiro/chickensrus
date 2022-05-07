import base64

from app import chickensrus
from app.forms import *
from app.models import *
from flask import render_template, escape, redirect, url_for, request, flash
from flask_login import current_user, login_user, logout_user, login_required


# Core routes
@chickensrus.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')


@chickensrus.route('/search', methods=['GET', 'POST'])
def search():
    query = request.form['query']
    results = search_listings(query)
    return render_template('search.html', results=results)


# Account routes
@chickensrus.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    image = base64.b64encode(current_user.picture).decode('ascii') if current_user.picture else None
    return render_template('account/account.html', current_user=current_user, image=image)


@chickensrus.route('/account/create', methods=['GET', 'POST'])
def account_create():
    account_create_form = AccountCreate()

    error = None
    if account_create_form.validate_on_submit():
        matching_user = query_user([account_create_form.username.data, account_create_form.email.data])
        if matching_user is not None:
            error = 'Account already exists.'
        else:
            new_user = User()
            new_user.username = account_create_form.username.data
            new_user.email = account_create_form.email.data
            new_user.set_password(account_create_form.password.data)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(request.args.get("next") or url_for('home'))

    return render_template('account/account_create.html', account_create_form=account_create_form, error=error)


@chickensrus.route('/login', methods=['GET', 'POST'])
def account_login():
    account_login_form = AccountLogin()

    error = None
    if account_login_form.validate_on_submit():
        user = query_user([account_login_form.username.data])
        if user is not None and user.password_matches(account_login_form.password.data):
            login_user(user)
            return redirect(request.args.get("next") or url_for('home'))
        else:
            error = 'Incorrect username or password.'

    return render_template('account/account_login.html', account_login_form=account_login_form, error=error)


@chickensrus.route('/account/logout', methods=['GET', 'POST'])
@login_required
def account_logout():
    logout_user()
    return redirect(url_for('home'))


@chickensrus.route('/account/edit', methods=['GET', 'POST'])
@login_required
def account_edit():
    account_edit_form = AccountEdit(
        first_name=current_user.first_name,
        last_name=current_user.last_name,
        username=current_user.username,
        email=current_user.email
    )

    error = None
    if account_edit_form.validate_on_submit():
        if current_user.password_matches(account_edit_form.password.data):
            current_user.picture = request.files[account_edit_form.picture.name].read()
            current_user.first_name = account_edit_form.first_name.data
            current_user.last_name = account_edit_form.last_name.data
            current_user.username = account_edit_form.username.data
            current_user.email = account_edit_form.email.data
            if account_edit_form.new_password.data:
                current_user.set_password(account_edit_form.new_password.data)
            db.session.add(current_user)
            db.session.commit()
            return redirect(url_for('home'))
        else:
            error = 'Incorrect password.'

    return render_template('account/account_edit.html', account_edit_form=account_edit_form, error=error)


@chickensrus.route('/account/delete', methods=['GET', 'POST'])
@login_required
def account_delete():
    account_delete_form = AccountDelete()

    if account_delete_form.is_submitted() and account_delete_form.confirm_deletion.data is True:
        db.session.delete(current_user)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('account/account_delete.html', account_delete_form=account_delete_form)


# Listing routes
@chickensrus.route('/listing/<int:listing_id>', methods=['GET', 'POST'])
def listing(listing_id):
    listing_id = escape(listing_id)
    matching_listing = query_listing(listing_id)

    if matching_listing is None:
        return render_template('error/404.html'), 404

    save_for_later_form = SaveForLater()
    if save_for_later_form.submit_SaveForLater.data and save_for_later_form.validate_on_submit():
        current_user.user_wishlist.append(matching_listing)
        db.session.add(current_user)
        db.session.commit()
        flash("Listing Saved")

    return render_template(
        'listing/listing.html',
        listing=matching_listing,
        save_for_later_form=save_for_later_form
    )


@chickensrus.route('/listing/create', methods=['GET', 'POST'])
@login_required
def listing_create():
    listing_create_form = ListingCreate()

    if listing_create_form.validate_on_submit():
        new_listing = Listing()
        new_listing.name = listing_create_form.name.data
        new_listing.description = listing_create_form.description.data
        new_listing.price = listing_create_form.price.data
        new_listing.picture = 'data:;base64,' + base64.b64encode(
            request.files[listing_create_form.picture.name].read()).decode('ascii')
        db.session.add(new_listing)
        db.session.commit()

        current_user.user_listings.append(new_listing)
        db.session.add(current_user)
        db.session.commit()

        return redirect(url_for('listing', listing_id=new_listing.id))

    return render_template('listing/listing_create.html', listing_create_form=listing_create_form)


@chickensrus.route('/wishlist', methods=['GET', 'POST'])
@login_required
def wishlist():
    count = len(current_user.user_wishlist)
    return render_template('wishlist.html', count=count)


@chickensrus.route('/wishlist/add/<int:listing_id>', methods=['GET', 'POST'])
@login_required
def wishlist_add(listing_id):
    listing_id = escape(listing_id)
    matching_listing = query_listing(listing_id)

    if matching_listing is None:
        return render_template('error/404.html'), 404

    current_user.user_wishlist.append(matching_listing)
    db.session.add(current_user)
    db.session.commit()
    return redirect(url_for('wishlist'))


@chickensrus.route('/wishlist/remove/<int:listing_id>t', methods=['GET', 'POST'])
@login_required
def wishlist_remove(listing_id):
    listing_id = escape(listing_id)
    matching_listing = query_listing(listing_id)

    if matching_listing is None:
        return render_template('error/404.html'), 404

    current_user.user_wishlist.remove(matching_listing)
    db.session.add(current_user)
    db.session.commit()
    return redirect(url_for('wishlist'))


@chickensrus.route('/wishlist/move/<int:listing_id>t', methods=['GET', 'POST'])
@login_required
def wishlist_move(listing_id):
    listing_id = escape(listing_id)
    matching_listing = query_listing(listing_id)

    if matching_listing is None:
        return render_template('error/404.html'), 404

    current_user.user_wishlist.remove(matching_listing)
    current_user.user_cart.append(matching_listing)
    db.session.add(current_user)
    db.session.commit()
    return redirect(url_for('wishlist'))


# Cart and checkout routes
@chickensrus.route('/cart', methods=['GET', 'POST'])
@login_required
def cart():
    count = 0
    subtotal = 0
    for listing in current_user.user_cart:
        count += 1
        subtotal += listing.price
    return render_template('cart.html', count=count, subtotal=subtotal)


@chickensrus.route('/cart/add/<int:listing_id>', methods=['GET', 'POST'])
@login_required
def cart_add(listing_id):
    listing_id = escape(listing_id)
    matching_listing = query_listing(listing_id)

    if matching_listing is None:
        return render_template('error/404.html'), 404

    current_user.user_cart.append(matching_listing)
    db.session.add(current_user)
    db.session.commit()
    return redirect(url_for('cart'))


@chickensrus.route('/cart/remove/<int:listing_id>', methods=['GET', 'POST'])
@login_required
def cart_remove(listing_id):
    listing_id = escape(listing_id)
    matching_listing = query_listing(listing_id)

    if matching_listing is None:
        return render_template('error/404.html'), 404

    current_user.user_cart.remove(matching_listing)
    db.session.add(current_user)
    db.session.commit()
    return redirect(url_for('cart'))


@chickensrus.route('/cart/move/<int:listing_id>', methods=['GET', 'POST'])
@login_required
def cart_move(listing_id):
    listing_id = escape(listing_id)
    matching_listing = query_listing(listing_id)

    if matching_listing is None:
        return render_template('error/404.html'), 404

    current_user.user_cart.remove(matching_listing)
    current_user.user_wishlist.append(matching_listing)
    db.session.add(current_user)
    db.session.commit()
    return redirect(url_for('cart'))


@chickensrus.route('/checkout', methods=['GET', 'POST'])
@login_required
def checkout():
    checkout_form = Checkout()

    if checkout_form.validate_on_submit():
        new_order = Order()
        new_order.first_name = checkout_form.first_name.data
        new_order.last_name = checkout_form.last_name.data
        new_order.email = checkout_form.email.data
        new_order.address = checkout_form.address.data
        new_order.city = checkout_form.city.data
        new_order.country = checkout_form.country.data
        new_order.zip_code = checkout_form.zip_code.data
        new_order.card_number = checkout_form.card_number.data
        new_order.card_exp = checkout_form.card_exp.data
        new_order.cart_cvv = checkout_form.card_cvv.data
        db.session.add(new_order)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('checkout.html', checkout_form=checkout_form)


# Error handlers
@chickensrus.errorhandler(404)
def page_not_found(e):
    return render_template('error/404.html'), 404
