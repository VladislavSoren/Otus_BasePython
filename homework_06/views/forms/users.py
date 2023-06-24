'''
Валидация полей на фронтенд
'''

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    name = StringField(
        label="User name:",
        validators=[
            DataRequired(),
            Length(min=3)
        ],
    )

    username = StringField(
        label="User username:",
        validators=[
            DataRequired(),
            Length(min=5)
        ],
    )
