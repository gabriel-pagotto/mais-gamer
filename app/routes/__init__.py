from app import app
from flask import request, redirect
from app.routes import admin, ajax, auth, cover, notices, posts, user, search

@app.before_request
def before_request():
  if app.config['FLASK_DEBUG'] != True:
    if request.url.startswith('http://'):
        url = request.url.replace('http://', 'https://', 1)
        code = 301
        return redirect(url, code=code)
