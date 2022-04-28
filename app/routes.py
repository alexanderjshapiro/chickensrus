from app import chickensrus
from app.forms import *
from app.models import User, db, query_user
from flask import render_template, escape, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required


@chickensrus.route('/')
def home():
    return render_template('home.html')


@chickensrus.route('/signup', methods=['GET', 'POST'])
def sign_up():
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
def sign_in():
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
def sign_out():
    logout_user()

    return redirect(url_for('home'))


@chickensrus.route('/account')
@login_required
def account():
    return render_template('account.html')


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
            current_user.image = form.image.data
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

    return render_template('account_edit.html', form=form, error=error)


@chickensrus.route('/account/delete', methods=['GET', 'POST'])
@login_required
def account_delete():
    form = AccountDelete()

    if form.is_submitted() and form.confirm_deletion.data is True:
        db.session.delete(current_user)
        db.session.commit()
        return redirect(url_for('home'))

    return render_template('account_delete.html', form=form)


@chickensrus.route('/listing/<int:listing_id>')
def listing(listing_id):
    return render_template('listing.html', listing_id=escape(listing_id))


@chickensrus.route('/cart')
def cart():
    return render_template('cart.html')


@chickensrus.route('/checkout')
def checkout():
    return render_template('checkout.html')
