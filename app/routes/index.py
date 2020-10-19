from app import app, database
from app.models import Posts, PostCategory, Users
from app.utils.date_time import DatePost
from flask import render_template, request, jsonify, redirect, url_for
from sqlalchemy import desc
from app.utils.index import return_url_category


@app.route('/', methods=['GET'])
def index():
    all_posts = Posts.query.order_by(desc('addedAt')).all()
    categories = PostCategory.query.all()
    users = Users.query.all()

    posts_list = []

    for post in all_posts:
        post_user = None
        post_category = None
        for user in users:
            if user.id == post.user_id:
                post_user = user
        for category in categories:
            if category.id == post.category:
                post_category = category.name

        post = {
            'id': post.id,
            'title': post.title,
            'subtitle': post.subtitle,
            'cover_image': post.cover_image,
            'addedAt': post.addedAt,
            'datePost': DatePost(post.addedAt),
            'category': {
                'name': post_category,
                'url': return_url_category(post.category),
            },
            'posted_by': {
                'username': post_user.username,
                'name': post_user.name,
                'surname': post_user.surname,
            },
        }

        posts_list.append(post)

    posts = {
        'pages': [],
    }

    posts_counter = 0
    page = {
        'header': None,
        'notices': []
    }

    for post in posts_list:
        posts_counter = posts_counter + 1
        if posts_counter == 1:
            page['header'] = post
        if posts_counter > 1 and posts_counter < 7:
            page['notices'].append(post)
        if posts_counter == 7:
            page['notices'].append(post)
            posts['pages'].append(page)
            page = {
                'header': None,
                'notices': []
            }
            posts_counter = 0

    page = request.args.get('page')

    if page != None:
        page = int(page)
        return jsonify({
            'pages': posts['pages'][page],
            'total': len(posts['pages']),
        })

    return render_template(
        'index.html',
        title='Mais Gamer',
        posts=posts,
    )


@app.route('/gaming-news', methods=['GET'])
def gaming_news():
    all_posts = Posts.query.order_by(desc('addedAt')).filter_by(category=1)
    users = Users.query.all()

    posts_list = []

    for post in all_posts:
        post_user = None
        for user in users:
            if user.id == post.user_id:
                post_user = user

        post = {
            'id': post.id,
            'title': post.title,
            'subtitle': post.subtitle,
            'cover_image': post.cover_image,
            'addedAt': post.addedAt,
            'datePost': DatePost(post.addedAt),
            'posted_by': {
                'username': post_user.username,
                'name': post_user.name,
                'surname': post_user.surname,
            },
        }

        posts_list.append(post)

    posts = {
        'pages': [],
    }

    posts_counter = 0
    page = {
        'header': None,
        'notices': []
    }

    for post in posts_list:
        posts_counter = posts_counter + 1
        if posts_counter == 1:
            page['header'] = post
        if posts_counter > 1 and posts_counter < 7:
            page['notices'].append(post)
        if posts_counter == 7:
            page['notices'].append(post)
            posts['pages'].append(page)
            page = {
                'header': None,
                'notices': []
            }
            posts_counter = 0

    page = request.args.get('page')

    if page != None:
        page = int(page)
        return jsonify({
            'pages': posts['pages'][page],
            'total': len(posts['pages']),
        })

    return render_template(
        'pages/categories.html',
        title='Mais Gamer - Gaming News',
        posts=posts,
    )


@app.route('/e-sports', methods=['GET'])
def e_sports():
    all_posts = Posts.query.order_by(desc('addedAt')).filter_by(category=2)
    users = Users.query.all()

    posts_list = []

    for post in all_posts:
        post_user = None
        for user in users:
            if user.id == post.user_id:
                post_user = user

        post = {
            'id': post.id,
            'title': post.title,
            'subtitle': post.subtitle,
            'cover_image': post.cover_image,
            'addedAt': post.addedAt,
            'datePost': DatePost(post.addedAt),
            'posted_by': {
                'username': post_user.username,
                'name': post_user.name,
                'surname': post_user.surname,
            },
        }

        posts_list.append(post)

    posts = {
        'pages': [],
    }

    posts_counter = 0
    page = {
        'header': None,
        'notices': []
    }

    for post in posts_list:
        posts_counter = posts_counter + 1
        if posts_counter == 1:
            page['header'] = post
        if posts_counter > 1 and posts_counter < 7:
            page['notices'].append(post)
        if posts_counter == 7:
            page['notices'].append(post)
            posts['pages'].append(page)
            page = {
                'header': None,
                'notices': []
            }
            posts_counter = 0

    page = request.args.get('page')

    if page != None:
        page = int(page)
        return jsonify({
            'pages': posts['pages'][page],
            'total': len(posts['pages']),
        })

    return render_template(
        'pages/categories.html',
        title='Mais Gamer - E-Sports',
        posts=posts,
    )


@app.route('/trailer', methods=['GET'])
def trailer():
    all_posts = Posts.query.order_by(desc('addedAt')).filter_by(category=3)
    users = Users.query.all()

    posts_list = []

    for post in all_posts:
        post_user = None
        for user in users:
            if user.id == post.user_id:
                post_user = user

        post = {
            'id': post.id,
            'title': post.title,
            'subtitle': post.subtitle,
            'cover_image': post.cover_image,
            'addedAt': post.addedAt,
            'datePost': DatePost(post.addedAt),
            'posted_by': {
                'username': post_user.username,
                'name': post_user.name,
                'surname': post_user.surname,
            },
        }

        posts_list.append(post)

    posts = {
        'pages': [],
    }

    posts_counter = 0
    page = {
        'header': None,
        'notices': []
    }

    for post in posts_list:
        posts_counter = posts_counter + 1
        if posts_counter == 1:
            page['header'] = post
        if posts_counter > 1 and posts_counter < 7:
            page['notices'].append(post)
        if posts_counter == 7:
            page['notices'].append(post)
            posts['pages'].append(page)
            page = {
                'header': None,
                'notices': []
            }
            posts_counter = 0

    page = request.args.get('page')

    if page != None:
        page = int(page)
        return jsonify({
            'pages': posts['pages'][page],
            'total': len(posts['pages']),
        })

    return render_template(
        'pages/categories.html',
        title='Mais Gamer - Trailers',
        posts=posts,
    )


@app.route('/stream', methods=['GET'])
def stream():
    return redirect(url_for('index'))
    all_posts = Posts.query.order_by(desc('addedAt')).filter_by(category=4)
    users = Users.query.all()

    posts_list = []

    for post in all_posts:
        post_user = None
        for user in users:
            if user.id == post.user_id:
                post_user = user

        post = {
            'id': post.id,
            'title': post.title,
            'subtitle': post.subtitle,
            'cover_image': post.cover_image,
            'addedAt': post.addedAt,
            'datePost': DatePost(post.addedAt),
            'posted_by': {
                'username': post_user.username,
                'name': post_user.name,
                'surname': post_user.surname,
            },
        }

        posts_list.append(post)

    posts = {
        'pages': [],
    }

    posts_counter = 0
    page = {
        'header': None,
        'notices': []
    }

    for post in posts_list:
        posts_counter = posts_counter + 1
        if posts_counter == 1:
            page['header'] = post
        if posts_counter > 1 and posts_counter < 7:
            page['notices'].append(post)
        if posts_counter == 7:
            page['notices'].append(post)
            posts['pages'].append(page)
            page = {
                'header': None,
                'notices': []
            }
            posts_counter = 0

    page = request.args.get('page')

    if page != None:
        page = int(page)
        return jsonify({
            'pages': posts['pages'][page],
            'total': len(posts['pages']),
        })

    return render_template(
        'pages/categories.html',
        title='Mais Gamer - Stream',
        posts=posts,
    )


@app.route('/strategy-guide', methods=['GET'])
def strategy_guide():
    all_posts = Posts.query.order_by(desc('addedAt')).filter_by(category=5)
    users = Users.query.all()

    posts_list = []

    for post in all_posts:
        post_user = None
        for user in users:
            if user.id == post.user_id:
                post_user = user

        post = {
            'id': post.id,
            'title': post.title,
            'subtitle': post.subtitle,
            'cover_image': post.cover_image,
            'addedAt': post.addedAt,
            'datePost': DatePost(post.addedAt),
            'posted_by': {
                'username': post_user.username,
                'name': post_user.name,
                'surname': post_user.surname,
            },
        }

        posts_list.append(post)

    posts = {
        'pages': [],
    }

    posts_counter = 0
    page = {
        'header': None,
        'notices': []
    }

    for post in posts_list:
        posts_counter = posts_counter + 1
        if posts_counter == 1:
            page['header'] = post
        if posts_counter > 1 and posts_counter < 7:
            page['notices'].append(post)
        if posts_counter == 7:
            page['notices'].append(post)
            posts['pages'].append(page)
            page = {
                'header': None,
                'notices': []
            }
            posts_counter = 0

    page = request.args.get('page')

    if page != None:
        page = int(page)
        return jsonify({
            'pages': posts['pages'][page],
            'total': len(posts['pages']),
        })

    return render_template(
        'pages/categories.html',
        title='Mais Gamer - Guias de estratégia',
        posts=posts,
    )


@app.route('/ads.txt', methods=['GET'])
def ads_text():
    return render_template('ads.txt')


@app.route('/articles/all', methods=['GET'])
def all_articles():
    page = request.args.get('page', 1, type=int)
    posts = Posts.query.order_by(desc('addedAt')).paginate(page, 12, False)

    next_url = url_for('all_articles', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('all_articles', page=posts.prev_num) \
        if posts.has_prev else None

    return render_template(
        'pages/all_articles.html',
        title='Todas as notícias',
        posts=posts.items,
        route='all_articles',
        num_posts=len(posts.items),
        posts_pages=posts,
        page_number=page,
        next_url=next_url,
        prev_url=prev_url,
    )
