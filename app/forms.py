from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, FileField
from wtforms.validators import *


class AccountCreate(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Invalid username.')])
    email = StringField('Email', validators=[DataRequired(message='Invalid email address.'), Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Invalid password.')])
    repeat_password = PasswordField('Repeat Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match.')
    ])
    submit = SubmitField('Create Account')


class AccountLogin(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Invalid username.')])
    password = PasswordField('Password', validators=[DataRequired(message='Invalid password.')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AccountEdit(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(message='Invalid password.')])

    picture = FileField('Image', validators=[
        FileAllowed(['jpg', 'jpe', 'jpeg', 'png', 'gif', 'svg', 'bmp'], 'Invalid file type.')
    ])
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    username = StringField('Username', validators=[DataRequired(message='Invalid username.')])
    email = StringField('Email', validators=[DataRequired(message='Invalid email address.'), Email()])
    new_password = PasswordField('New Password')
    repeat_password = PasswordField(
        'Repeat Password',
        validators=[EqualTo('new_password', message='Passwords must match.')]
    )
    submit = SubmitField('Save')


class AccountDelete(FlaskForm):
    confirm_deletion = BooleanField('Confirm Deletion')
    submit = SubmitField('Delete Account')


class PostListing(FlaskForm):
    listingTitle = StringField('Item', validators=[DataRequired(message='Title of Item needed')])
    listingPrice = DecimalField('Price', validators=[DataRequired(message='Price of Item needed')])
    listingDescription = StringField('Description')
    listingPicture = FileField('Upload Image', validators=[
        FileAllowed(['jpg', 'jpe', 'jpeg', 'png', 'gif', 'svg', 'bmp'], 'Invalid file type.')])
    submit = SubmitField('Publish Listing')


class SaveListing(FlaskForm):
    submit = SubmitField("Save to Wishlist")
