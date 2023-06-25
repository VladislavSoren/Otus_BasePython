'''
Валидация полей на фронтенд
'''

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class UserForm(FlaskForm):
    name = StringField(
        label="Name:",
        validators=[
            DataRequired(),
            Length(min=3)
        ],
    )

    username = StringField(
        label="Username:",
        validators=[
            DataRequired(),
            Length(min=5)
        ],
    )

    email = StringField(
        label="Email:",
        validators=[
            DataRequired(),
            Length(min=5)
        ],
    )

    profession_type = StringField(
        label="Profession:",
        validators=[
            DataRequired(),
            Length(min=5)
        ],
    )

    website = StringField(
        label="Website:",
        validators=[
            DataRequired(),
            Length(min=5)
        ],
    )
