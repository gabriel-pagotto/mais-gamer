from flask import json
from app import app, database
from app.models import Files
from flask import request, jsonify
from app.utils.aws_s3 import save_image_and_get_url


@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['file']
    file_url = save_image_and_get_url(file)
    file_returned = Files(
      url = file_url,
    )

    database.session.add(file_returned)
    database.session.commit()

    return jsonify({ 'url': file_url })
