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


# Other Forms
class Checkout(FlaskForm):
    first_name = StringField('First Name', render_kw={'class': "form-control"})
    last_name = StringField('Last Name', render_kw={'class': "form-control"})
    # Validators used to require all inputted information before able to submit
    email = StringField('Email', validators=[DataRequired(message='Invalid email address.'), Email()],
                        render_kw={'class': "form-control"})
    address = StringField('Address', validators=[DataRequired(message='Invalid address.')],
                          render_kw={'class': "form-control"})
    city = StringField('City', validators=[DataRequired(message='Please input city.')],
                       render_kw={'class': "form-control"})
    country = StringField('Country', validators=[DataRequired(message='Please input country.')],
                          render_kw={'class': "form-control"})
    zip_code = StringField('Zip Code', validators=[DataRequired(message='Please input zip code.')],
                           render_kw={'class': "form-control"})
    card_number = StringField('Card Number', validators=[DataRequired(message='Please input card number.')],
                              render_kw={'class': "form-control"})
    card_exp = StringField('Card Expiration Date',
                           validators=[DataRequired(message='Please input card expiration date.')],
                           render_kw={'class': "form-control"})
    card_cvv = StringField('CVV', validators=[DataRequired(message='Please input card security code.')],
                           render_kw={'class': "form-control"})
    submit = SubmitField('Submit Order', render_kw={'class': "btn btn-danger w-100"})
