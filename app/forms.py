from flask_wtf import FlaskForm
from flask_wtf.file import *
from wtforms import StringField, PasswordField, BooleanField, SubmitField
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


class AccountEdit(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired(message='Invalid password.')])

    image = FileField('Image', validators=[
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
