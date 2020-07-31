from app import database
from app.models import Users, Posts, Games
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

class NewPostForm(FlaskForm):
    title = StringField(validators=[DataRequired()])
    subtitle = StringField(validators=[DataRequired()])
    cover_image = FileField(validators=[FileRequired()])
    game_id = SelectField(validators=[DataRequired()])
    pc_image = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Somente imagens JPG e PNG!')])  
    pc_text = TextAreaField()
    pc_last_image = FileField(validators=[FileRequired(), FileAllowed(['jpg', 'png'], 'Somente imagens JPG e PNG!')])
    pc_last_text = TextAreaField(DataRequired())
    is_esport = BooleanField()
    source_name = StringField(validators=[DataRequired()])
    source_url = StringField(validators=[DataRequired()])
    submit = SubmitField()

class NewPostFormTest(FlaskForm):
    title = StringField(validators=[DataRequired()])
    subtitle = StringField(validators=[DataRequired()])
    cover_image = FileField(validators=[DataRequired(), FileRequired()])
    game_id = SelectField(validators=[DataRequired()])
    post_content = TextAreaField(validators=[DataRequired()])
    is_esport = BooleanField()
    submit = SubmitField()

class ProfileForm(FlaskForm):
    username = StringField(validators=[DataRequired()])
    name = StringField(validators=[DataRequired()])
    surname = StringField(validators=[DataRequired()])
    email = StringField(validators=[DataRequired()])
    submit = SubmitField()
