import json, pytz
from app import app
from app.models import Users, Posts, Games, Post_Content
from datetime import datetime
from flask import render_template, redirect, flash, request, url_for, jsonify
from sqlalchemy import desc
from app.utils.date_time import DatePost

@app.route('/hours', methods=["GET"])
def hours():

    def datetime_sao_paulo():
        utc_time = datetime.utcnow()
        tz = pytz.timezone('America/Sao_Paulo')
        utc_time =utc_time.replace(tzinfo=pytz.UTC) 
        st_john_time=utc_time.astimezone(tz)
        return st_john_time
    
    hours = (datetime_sao_paulo())
    print(hours)
    return jsonify({
    "hours": hours,
    "hours_now": datetime.utcnow(),
    })

@app.route('/ajax', methods=["GET"])
def ajax():
    return render_template('ajax.html', title='ajax')

@app.route('/notícias/páginação', methods=['GET'])
def load_more_notices():
    page = request.args.get('page', 1, type=int)
    posts_pages = Posts.query.order_by(desc('addedAt')).paginate(page, 8, True)
    posts = posts_pages.items

    all_posts = []

    for post in posts:
        post_data = {
            'id': post.id,
            'title': post.title,
            'subtitle': post.subtitle,
            'cover_image': post.cover_image,
            'user_id': post.user_id,
            'game_id': post.game_id,
            'addedAt': DatePost(post.addedAt),
            'views': post.views,
            'is_esport': post.is_esport,
        }

        all_posts.append(post_data)

        data = {
            'total_pages': posts_pages.pages,
            'data': all_posts,
        }


    return jsonify(data)

@app.route('/notícias/<name>/páginação', methods=['GET'])
def load_more_notices_by_game(name):
    page = request.args.get('page', 1, type=int)
    try:
        game = Games.query.filter_by(name = name).first()
        posts_pages = Posts.query.filter_by(game_id = game.id).order_by(desc('addedAt')).paginate(page, 8, True)
    except AttributeError:
        return redirect(url_for('notices'))
    
    if game.id == 0:
        return redirect(url_for('index'))

    all_posts = []

    posts = posts_pages.items

    for post in posts:
        post_data = {
            'id': post.id,
            'title': post.title,
            'subtitle': post.subtitle,
            'cover_image': post.cover_image,
            'user_id': post.user_id,
            'game_id': post.game_id,
            'addedAt': DatePost(post.addedAt),
            'views': post.views,
            'is_esport': post.is_esport,
        }

        all_posts.append(post_data)

        data = {
            'total_pages': posts_pages.pages,
            'data': all_posts,
        }

    return jsonify(data)

@app.route('/eSports/páginação', methods=['GET'])
def load_more_eSports():
    page = request.args.get('page', 1, type=int)
    posts_pages = Posts.query.filter_by(is_esport = 1).order_by(desc('addedAt')).paginate(page, 8, True)
    posts = posts_pages.items

    all_posts = []

    for post in posts:
        post_data = {
            'id': post.id,
            'title': post.title,
            'subtitle': post.subtitle,
            'cover_image': post.cover_image,
            'user_id': post.user_id,
            'game_id': post.game_id,
            'addedAt': DatePost(post.addedAt),
            'views': post.views,
            'is_esport': post.is_esport,
        }

        all_posts.append(post_data)

        data = {
            'total_pages': posts_pages.pages,
            'data': all_posts,
        }


    return jsonify(data)
