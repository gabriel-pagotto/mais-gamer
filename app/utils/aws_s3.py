import boto3
from app import app, database
from app.aws.s3 import s3
from app.models import Files


def take_last_object():
    all_objects = []
    for file in s3.objects.all():
        file_parts = file.key.split('.')
        file_number = int(file_parts[0])
        all_objects.append(file_number)

    return sorted(all_objects)[-1]


def save_image_and_get_url(file):
    ext = file.filename.split('.')[-1]
    number = int(take_last_object() + 1)
    file_number = str(number)
    file_name = (file_number + '.' + ext)
    s3.Object(file_name).put(ACL='public-read', Body=file)
    return 'https://' + app.config['S3_BUCKET_NAME'] + '.s3.' + app.config['AWS_REGION'] + '.amazonaws.com/' + file_name


def delete_file(file_url):
    key = file_url.split('/')[-1]
    client = boto3.client('s3')
    client.delete_object(Bucket=app.config['S3_BUCKET_NAME'], Key=key)


def filesDatabaseControl(file_url):
    file = Files.query.filter_by(url=file_url).first()
    if file is None:
        return
    if file.used == 1:
        database.session.delete(file)
    if file.used == 0:
        delete_file(file.url)
        database.session.delete(file)


def clearUploadCache():
    files = Files.query.all()

    for file in files:
        filesDatabaseControl(file.url)
    database.session.commit()
