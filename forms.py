from flask_wtf import FlaskForm
from wtforms import StringField, TelField, EmailField, IntegerField, SubmitField
from wtforms.validators import DataRequired, InputRequired, equal_to, email, length, ValidationError

class ApplicationForm(FlaskForm):
    Fullname = StringField('FullName', validators=[DataRequired(), length(min=2, max=25)])
    Email = EmailField('Email', validators=[DataRequired(), email() ])
    PhoneNumber = IntegerField('PhoneNumber', validators=[DataRequired(), length(min=9, max=10)])
    Street = IntegerField('Address', validators=[DataRequired(), length(min=8)])
    SSN = IntegerField('SSN', validators=[DataRequired(), length(min=9, max=9)])