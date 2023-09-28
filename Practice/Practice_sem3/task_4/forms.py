
from flask_wtf import FlaskForm
from wtforms import StringField, EmailField
from wtforms.validators import DataRequired, Email, EqualTo


class RegisterForm(FlaskForm):
    user_name = StringField('username', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])
    password = StringField('password', validators=[DataRequired()])
    confirm_password = StringField('password', validators=[DataRequired(), EqualTo('password')])