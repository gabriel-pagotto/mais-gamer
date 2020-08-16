from flask import Flask, redirect, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sslify import SSLify


app = Flask(__name__)
sslify = SSLify(app)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config.from_object(Config)
database = SQLAlchemy(app)
migrate = Migrate(app, database)
login = LoginManager(app)
login.login_view = 'login'


from app import routes, models
