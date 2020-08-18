import boto3
from app import app, database
from app.aws.s3 import s3
from app.models import Image


def take_last_object():
    all_objects = []
    for file in s3.objects.all():
        file_parts = file.key.split('.')
        file_number = int(file_parts[0])
        all_objects.append(file_number)

    return sorted(all_objects)[-1]


def save_image_and_get_url(filename):
    number = int(take_last_object() + 1)
    image_number = str(number)
    image_name = (image_number + '.png')
    s3.Object(image_name).put(ACL='public-read', Body=filename)
    return 'https://' + app.config['S3_BUCKET_NAME'] + '.s3.' + app.config['AWS_REGION'] + '.amazonaws.com/' + image_name


def delete_image(image_url):
    key = image_url.split('/')[-1]
    client = boto3.client('s3')
    client.delete_object(Bucket=app.config['S3_BUCKET_NAME'], Key=key)

def imagesDatabaseControl(image_url):
    image = Image.query.filter_by(url=image_url).first()
    if image is None:
        return
    if image.used == 1:
        database.session.delete(image)
    if image.used == 0:
      delete_image(image.url)
      database.session.delete(image)

def clearUploadImageCache():
  images = Image.query.all()

  for image in images:
      imagesDatabaseControl(image.url)
  database.session.commit()
