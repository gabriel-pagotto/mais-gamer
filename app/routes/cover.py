import os
from app import app
from app.models import Posts, Games
from app.utils.date_time import DatePost
from app.utils.header_games import header_games
from app.utils.limit_notices import limit_notices
from flask import render_template, redirect, flash, request, url_for

@app.route('/', methods=['GET'])
def index():
    posts = Posts.query.all()
    last_notices = []
    for post in posts:
        last_notices.append(post)
    last_notices.reverse()
    last_notice = last_notices[0]
    rest_notices = [last_notices[1], last_notices[2], last_notices[3]]

    games = Games.query.order_by('name').all()

    del(last_notices[0])
    del(last_notices[0])
    del(last_notices[0])
    del(last_notices[0])

    return render_template(
        'index.html',
        title = 'Página inicial',
        last_notice = last_notice,
        rest_notices = rest_notices,
        last_notices = last_notices,
        games = games,
        DatePost = DatePost,
        header_games = header_games,
        limit_notices = limit_notices,
    )

@app.route('/user', methods=['GET'])
def user():
    return 'user'

@app.route('/config', methods=['GET'])
def config():
    return 'config'
