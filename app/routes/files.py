from flask import json
from app import app
from flask import request, jsonify
from app.utils.aws_s3 import save_image_and_get_url, delete_image


@app.route("/upload", methods=['POST'])
def upload():
    file = request.files['file']
    url = save_image_and_get_url(file)
    return jsonify({ 'url': url })
