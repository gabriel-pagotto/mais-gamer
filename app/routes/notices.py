import os
from app import app
from app.models import Users, Posts, Games, Post_Content
from app.utils.date_time import DatePost
from app.utils.url_for_notices import url_for_notices
from app.utils.header_games import header_games
from flask import render_template, redirect, flash, request, url_for
from sqlalchemy import desc

@app.route('/notices', methods=['GET'])
def notices():
    page = request.args.get('page', 1, type=int)
    posts_pages = Posts.query.order_by(desc('addedAt')).paginate(page, 8, True)
    posts = posts_pages.items

    next_url = url_for('notices', page=posts_pages.next_num) \
        if posts_pages.has_next else None
    prev_url  = url_for('notices', page=posts_pages.prev_num) \
        if posts_pages.has_prev else None

    return render_template(
        'notices/notices.html',
        title = 'Todas as notícias',
        def_name = 'notices',
        notices = posts,
        DatePost = DatePost,
        posts_pages = posts_pages,
        page_number = page,
        next_url = next_url,
        prev_url = prev_url,
        url_for_notices = url_for_notices,
        last_param = None,
        header_games = header_games,
    )

@app.route('/notices/<name>', methods=['GET'])
def notices_by_game(name):
    page = request.args.get('page', 1, type=int)
    try:
        game = Games.query.filter_by(name = name).first()
        posts = Posts.query.filter_by(game_id = game.id).order_by(desc('addedAt')).paginate(page, 8, True)
    except AttributeError:
        return redirect(url_for('notices'))
    
    if game.id == 0:
        return redirect(url_for('index'))
    
    next_url = url_for('notices_by_game', name=name, page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('notices_by_game', name=name, page=posts.prev_num) \
        if posts.has_prev else None

    return render_template(
        'notices/notices.html',
        title = game.name,
        def_name = 'notices_by_game',
        notices = posts.items,
        game = game,
        DatePost = DatePost,
        posts_pages = posts,
        page_number = page,
        next_url = next_url,
        prev_url = prev_url,
        url_for_notices = url_for_notices,
        last_param = game.name,
        header_games = header_games,
    )

@app.route('/notice/<id>', methods=['GET'])
def notice(id):
    post = Posts.query.filter_by(id = id).first()
    post_content = Post_Content.query.filter_by(post_id = id)
    game = Games.query.filter_by(id = post.game_id).first()
    user = Users.query.filter_by(id = post.user_id).first()

    return render_template (
        'notices/notice.html',
        title = post.title,
        notice = post,
        notice_content = post_content,
        user = user,
        DatePost = DatePost,
        game = game,
        header_games = header_games,
    )
