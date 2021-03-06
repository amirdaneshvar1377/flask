from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms import PasswordField, StringField, TextField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])


class RegisterForm(FlaskForm):
    full_name = StringField()
    email = EmailField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    password_confirm = PasswordField(validators=[DataRequired()])


class SearchForm(FlaskForm):
    search_query = TextField(validators=[DataRequired])
