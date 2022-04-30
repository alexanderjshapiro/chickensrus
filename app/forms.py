from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DecimalField, FileField
from wtforms.validators import *


class SignUp(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Invalid username.')])
    email = StringField('Email', validators=[DataRequired(message='Invalid email address.'), Email()])
    password = PasswordField('Password', validators=[DataRequired(message='Invalid password.')])
    repeat_password = PasswordField('Repeat Password', validators=[
        DataRequired(),
        EqualTo('password', message='Passwords must match.')
    ])
    submit = SubmitField('Sign Up')


class SignIn(FlaskForm):
    username = StringField('Username', validators=[DataRequired(message='Invalid username.')])
    password = PasswordField('Password', validators=[DataRequired(message='Invalid password.')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class DeleteAccount(FlaskForm):
    confirm_deletion = BooleanField('Confirm Deletion')
    submit = SubmitField('Delete Account')

class PostListing(FlaskForm):
    listingTitle = StringField('Item', validators=[DataRequired(message='Title of Item needed')])
    listingPrice = DecimalField('Price', validators=[DataRequired(message='Price of Item needed')])
    listingDescription = StringField('Description')
    listingPicture = FileField('Upload Image', validators=[FileAllowed(['jpg', 'jpe', 'jpeg', 'png', 'gif', 'svg', 'bmp'], 'Invalid file type.')])
    submit = SubmitField('Publish Listing')
