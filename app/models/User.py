from app import database, login
from app.utils.date_time import datetime_sao_paulo
from flask_login import UserMixin

class Users(UserMixin, database.Model):
    id = database.Column(database.Integer, primary_key=True)
    username = database.Column(database.String(16), unique=True)
    name = database.Column(database.String(20))
    surname = database.Column(database.String(60))
    email = database.Column(database.String(120), unique=True)
    password = database.Column(database.String(128))
    createdAt = database.Column(database.DateTime, default=datetime_sao_paulo())
    is_admin = database.Column(database.Boolean, default=False)
    is_poster = database.Column(database.Boolean, default=False)

    def __repr__(self):
        return '<Users {}>'.format(self.users)
    
    @login.user_loader
    def load_user(id):
        return Users.query.get(int(id))
