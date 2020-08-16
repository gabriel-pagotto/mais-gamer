import boto3
from app import app

s3 = boto3.resource(
    's3',
    aws_access_key_id=app.config['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=app.config['AWS_SECRET_ACCESS_KEY'],
).Bucket(app.config['S3_BUCKET_NAME'])
