from flask import json
from app import app, database
from app.models import Image
from flask import request, jsonify
from app.utils.aws_s3 import save_image_and_get_url


@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['file']
    url = save_image_and_get_url(file)
    image = Image(
      url = url,
    )

    database.session.add(image)
    database.session.commit()

    return jsonify({ 'url': url })
