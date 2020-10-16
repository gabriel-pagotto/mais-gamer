from app import app, database
from flask import jsonify, url_for, request
from app.models import Posts, PostCategory, Users, Post_Content
from app.utils.date_time import DatePost
from sqlalchemy import desc
from app.utils.index import return_url_category

@app.route('/api/articles/all', methods=['GET'])
def api_all_articles():
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

    return jsonify({
      'response': posts_list,
    })

@app.route('/api/articles/contents', methods=['GET'])
def api_get_contents():
    id = request.args.get('q')
    all_contents = Post_Content.query.filter_by(post_id=id).order_by('position')

    contents = []

    for content in all_contents:
        contents.append({
          'content': content.content,
          'position': content.position,
          'type': content.type,
        })

    return jsonify({
      'response': contents,
    })
