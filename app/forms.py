from app import database
from app.models import Users, Posts
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField, SelectField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, InputRequired, ValidationError


class LoginForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()


class RegisterForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    name = StringField(validators=[DataRequired()])
    surname = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    password = PasswordField(validators=[DataRequired()])
    confirm_password = PasswordField(validators=[DataRequired()])
    submit = SubmitField()

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Este nome de usuário já existe.')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Este email já existe.')


class ProfileForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    name = StringField(validators=[DataRequired()])
    surname = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    submit = SubmitField()
