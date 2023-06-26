'''
Валидация полей на фронтенд
'''

from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length


class PostProjForm(FlaskForm):
    user_id = StringField(
        label="Your ID:",
        validators=[
            DataRequired(),
            Length(min=1)
        ],
    )

    title = StringField(
        label="Name of post:",
        validators=[
            DataRequired(),
            Length(min=3)
        ],
    )

    body = StringField(
        label="Brief introduction:",
        validators=[
            DataRequired(),
            Length(min=5)
        ],
    )

    proj_name = StringField(
        label="Project name:",
        validators=[
            DataRequired(),
            Length(min=5)
        ],
    )

    description = StringField(
        label="Description:",
        validators=[
            DataRequired(),
            Length(min=5)
        ],
    )

    url = StringField(
        label="Project URL:",
        validators=[
            DataRequired(),
            Length(min=5)
        ],
    )

    other_contributors = StringField(
        label="Names other contributors:",
    )
