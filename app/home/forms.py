from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email
from ..models import Link


class ShortenUrlForm(FlaskForm):
    """
    Form for users to create new account
    """
    url = StringField('URL')
    submit = SubmitField('Shorten')
