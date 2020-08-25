import random
from app import app, database
from app.models import Users, Posts, Games, Post_Content
from app.utils.url_for_notices import url_for_notices
from flask import render_template, redirect, request, url_for
from sqlalchemy import desc


@app.route('/notícias', methods=['GET'])
def notices():
    page = request.args.get('page', 1, type=int)
    posts_pages = Posts.query.order_by(desc('addedAt')).paginate(page, 8, True)
    posts = posts_pages.items

    next_url = url_for('notices', page=posts_pages.next_num) \
        if posts_pages.has_next else None
    prev_url = url_for('notices', page=posts_pages.prev_num) \
        if posts_pages.has_prev else None

    return render_template(
        'notices/notices.html',
        title='Todas as notícias',
        def_name='notices',
        notices=posts,
        posts_pages=posts_pages,
        page_number=page,
        next_url=next_url,
        prev_url=prev_url,
        url_for_notices=url_for_notices,
        last_param=None,
    )


@app.route('/notícias/<name>', methods=['GET'])
def notices_by_game(name):
    page = request.args.get('page', 1, type=int)
    try:
        game = Games.query.filter_by(name=name).first()
        posts = Posts.query.filter_by(game_id=game.id).order_by(
            desc('addedAt')).paginate(page, 8, True)
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
        title=game.name,
        def_name='notices_by_game',
        notices=posts.items,
        game=game,
        posts_pages=posts,
        page_number=page,
        next_url=next_url,
        prev_url=prev_url,
        url_for_notices=url_for_notices,
        last_param=game.name,
    )


@app.route('/eSports', methods=['GET'])
def notices_eSports():
    page = request.args.get('page', 1, type=int)
    posts_pages = Posts.query.filter_by(is_esport=1).order_by(
        desc('addedAt')).paginate(page, 8, True)
    posts = posts_pages.items

    return render_template(
        'notices/notices.html',
        title='Todas as notícias',
        def_name='notices',
        notices=posts,
        posts_pages=posts_pages,
    )


@app.route('/notícia/<id>', methods=['GET'])
def notice(id):
    all_posts = Posts.query.all()
    all_posts_array = []
    for post in all_posts:
        if post.id != id:
            all_posts_array.append(post)

    num_randons = []

    while len(num_randons) < 4:
        if len(num_randons) == 0:
            num_randons.append(random.randint(0, len(all_posts_array) - 1))
        if len(num_randons) == 1:
            num_selected = random.randint(0, len(all_posts_array) - 1)
            if num_selected != num_randons[0]:
                num_randons.append(num_selected)
        if len(num_randons) == 2:
            num_selected = random.randint(0, len(all_posts_array) - 1)
            if num_selected != num_randons[0] and num_selected != num_randons[1]:
                num_randons.append(num_selected)
        if len(num_randons) == 3:
            num_selected = random.randint(0, len(all_posts_array) - 1)
            if num_selected != num_randons[0] and num_selected != num_randons[1] and num_selected != num_randons[2]:
                num_randons.append(num_selected)

    more_news = []

    for num in num_randons:
        more_news.append(all_posts_array[num])

    post = Posts.query.filter_by(id=id).first()
    post_content = Post_Content.query.filter_by(post_id=id).order_by('position')
    game = Games.query.filter_by(id=post.game_id).first()
    user = Users.query.filter_by(id=post.user_id).first()

    if post.views == None or not post.views:
        post.views = 1
    else:
        post.views = post.views + 1

    database.session.commit()

    return render_template(
        'notices/notice.html',
        title=post.title,
        notice=post,
        notice_content=post_content,
        user=user,
        game=game,
        more_news=more_news,
    )
