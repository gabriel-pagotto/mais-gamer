from app.aws.s3 import s3

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
