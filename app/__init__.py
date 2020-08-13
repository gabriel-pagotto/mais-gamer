from flask import Flask, redirect, request
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sslify import SSLify

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
app.config.from_object(Config)
database = SQLAlchemy(app)
migrate = Migrate(app, database)
login = LoginManager(app)
login.login_view = 'login'

@app.before_request
def before_request():
    if not request.is_secure and app.config['DEBUG'] != True:
        url = request.url.replace("http://", "https://", 1)
        code = 301
        return redirect(url, code=code)

from app import routes, models
