
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,DateField,TextAreaField,SelectField
from wtforms.validators import DataRequired,InputRequired,ValidationError,Length,EqualTo,Email
from flask_login import current_user
from app.models import User

class LoginForm(FlaskForm):
    username = StringField("Username",validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit = SubmitField("Submit")

class Notification(FlaskForm):
    content = StringField("Content",validators=[])
    fb_group = StringField("Group",validators=[])
