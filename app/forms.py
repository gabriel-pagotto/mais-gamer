from app import database
from app.models import Users, Posts, Games
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, FileField, SelectField, TextAreaField
from wtforms.validators import data_required, InputRequired, ValidationError

class LoginForm(FlaskForm):
    username = StringField(validators=[data_required()])
    password = PasswordField(validators=[data_required()])
    submit = SubmitField()

class RegisterForm(FlaskForm):
    username = StringField(validators=[data_required()])
    name = StringField(validators=[data_required()])
    surname = StringField(validators=[data_required()])
    email = StringField(validators=[data_required()])
    password = PasswordField(validators=[data_required()])
    confirm_password = PasswordField(validators=[data_required()])
    submit = SubmitField()

    def validate_username(self, username):
        user = Users.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Este nome de usuário já existe.')

    def validate_email(self, email):
        user = Users.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Este email já existe.')

class NewPostForm(FlaskForm):
    title = StringField(validators=[data_required()])
    subtitle = StringField(validators=[data_required()])
    cover_image = FileField(validators=[FileRequired()])
    game_id = SelectField(validators=[data_required()])
    pc_image = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Somente imagens JPG e PNG!')])  
    pc_text = TextAreaField()
    pc_last_image = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Somente imagens JPG e PNG!')])
    pc_last_text = TextAreaField(data_required())
    submit = SubmitField()

class ProfileForm(FlaskForm):
    username = StringField(validators=[data_required()])
    name = StringField(validators=[data_required()])
    surname = StringField(validators=[data_required()])
    email = StringField(validators=[data_required()])
    submit = SubmitField()
