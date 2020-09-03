from app import app, database
from app.models import Posts, PostCategory, Users
from app.utils.date_time import DatePost
from flask import render_template, request, jsonify, redirect, url_for
from sqlalchemy import desc
from app.utils.index import return_url_category


@app.route('/', methods=['GET'])
def index():
    all_posts = Posts.query.order_by(desc('addedAt')).all()
    users = Users.query.all()

    posts_list = []

    for post in all_posts:
        post_user = ''
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
            'category': {
                'name': PostCategory.query.filter_by(id=post.category).first().name,
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
        'header': '',
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
                'header': '',
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
        title='Mais Gamer - Notícias para Gamers',
        posts=posts,
    )


@app.route('/gaming-news', methods=['GET'])
def gaming_news():
    all_posts = Posts.query.order_by(desc('addedAt')).filter_by(category=1)
    users = Users.query.all()

    posts_list = []

    for post in all_posts:
        post_user = ''
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
        'header': '',
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
                'header': '',
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
    return redirect(url_for('index'))
    all_posts = Posts.query.order_by(desc('addedAt')).filter_by(category=2)
    users = Users.query.all()

    posts_list = []

    for post in all_posts:
        post_user = ''
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
        'header': '',
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
                'header': '',
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
        post_user = ''
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
        'header': '',
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
                'header': '',
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
        post_user = ''
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
        'header': '',
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
                'header': '',
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
