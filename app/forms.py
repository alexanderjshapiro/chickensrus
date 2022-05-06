from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, FileField
from wtforms.validators import *


# Account Forms
class AccountCreate(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Invalid username.')])
    email = StringField('Email', validators=[DataRequired(message='Invalid email address.'), Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Invalid password.')])
    repeat_password = PasswordField('Repeat Password',
                                    validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
    submit = SubmitField('Create Account')


class AccountLogin(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Invalid username.')])
    password = PasswordField('Password', validators=[DataRequired(message='Invalid password.')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AccountEdit(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(message='Invalid password.')])

    picture = FileField('Image', validators=[
        FileAllowed(['jpg', 'jpe', 'jpeg', 'png', 'gif', 'svg', 'bmp'], 'Invalid file type.')])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    username = StringField('Username', validators=[DataRequired(message='Invalid username.')])
    email = StringField('Email', validators=[DataRequired(message='Invalid email address.'), Email()])
    new_password = PasswordField('New Password')
    repeat_password = PasswordField('Repeat Password',
                                    validators=[EqualTo('new_password', message='Passwords must match.')])
    submit = SubmitField('Save')


class AccountDelete(FlaskForm):
    confirm_deletion = BooleanField('Confirm Deletion')
    submit = SubmitField('Delete Account')


# Listing Forms
class ListingCreate(FlaskForm):
    name = StringField('Item', validators=[DataRequired(message='Title of Item needed')])
    price = DecimalField('Price', validators=[DataRequired(message='Price of Item needed')])
    description = StringField('Description')
    picture = FileField('Upload Image', validators=[
        FileAllowed(['jpg', 'jpe', 'jpeg', 'png', 'gif', 'svg', 'bmp'], 'Invalid file type.')])
    submit = SubmitField('Publish Listing')


class SaveForLater(FlaskForm):
    submit_SaveForLater = SubmitField("Save to Wishlist")


class AddToCart(FlaskForm):
    submit_AddToCart = SubmitField('Add to Cart')


# Other Forms
class Checkout(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    # Validators used to require all inputted information before able to submit
    email = StringField('Email', validators=[DataRequired(message='Invalid email address.'), Email()])
    address = StringField('Address', validators=[DataRequired(message='Invalid address.')])
    city = StringField('City', validators=[DataRequired(message='Please input city.')])
    country = StringField('Country', validators=[DataRequired(message='Please input country.')])
    zip_code = StringField('Zip Code', validators=[DataRequired(message='Please input zip code.')])
    card_number = StringField('Card Number', validators=[DataRequired(message='Please input card number.')])
    card_exp = StringField('Card Expiration Date',
                           validators=[DataRequired(message='Please input card expiration date.')])
    card_cvv = StringField('CVV', validators=[DataRequired(message='Please input card security code.')])
    submit = SubmitField('Submit Order')
  
