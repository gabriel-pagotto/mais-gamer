import os
from dotenv import load_dotenv
load_dotenv()

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = bool(os.getenv('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True' )
    SECRET_KEY = os.getenv('SECRET_KEY')
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = os.getenv('AWS_REGION')
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')
    USE_S3_DEBUG = bool(os.getenv('USE_S3_DEBUG') == 'True')
    FLASK_DEBUG = os.getenv('FLASK_DEBUG')
    HTTPS_REDIRECT = os.getenv('HTTPS_REDIRECT')
    PORT = int(os.environ.get('PORT', 7000))
