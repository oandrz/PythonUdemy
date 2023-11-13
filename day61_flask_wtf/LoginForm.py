from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


class LoginForm(FlaskForm):
    # The validators parameter accepts a List of validator Objects.
    email = StringField(
        label='email',
        validators=[
            DataRequired(),
            Email(message="Invalid email address")
        ]
    )
    password = PasswordField(
        label='password',
        validators=[
            DataRequired(),
            Length(min=8, message="Password must be at least 8 characters")
        ]
    )
    submit = SubmitField(label='Log In')
