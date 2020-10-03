import json
import requests
from app import app, database
from app.models import Posts, Post_Content, Files
from app.utils.aws_s3 import delete_file, clearUploadCache
from app.utils.sub_header_options import sub_header
from bs4 import BeautifulSoup
from flask import render_template, redirect, request, url_for, jsonify
from flask_login import current_user, login_required
from sqlalchemy import desc


@app.route('/posts', methods=['GET'])
@login_required
def posts():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if current_user.is_admin != 1 and current_user.is_poster != 1:
        return redirect(url_for('index'))
    page = request.args.get('page', 1, type=int)
    posts = Posts.query.filter_by(user_id=current_user.id).order_by(
        desc('addedAt')).paginate(page, 9, True)

    next_url = url_for('posts', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('posts', page=posts.prev_num) \
        if posts.has_prev else None

    return render_template(
        'pages/posts/posts.html',
        title='Postagens',
        selected='posts',
        sub_header=sub_header(1, 'posts'),
        posts=posts.items,
        num_posts=len(posts.items),
        posts_pages=posts,
        page_number=page,
        next_url=next_url,
        prev_url=prev_url,
    )


@app.route('/posts/new', methods=['GET', 'POST'])
@login_required
def post_new():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if current_user.is_admin != 1 and current_user.is_poster != 1:
        return redirect(url_for('index'))

    if request.method == 'POST':
        data = json.loads(request.data)
        contents = []

        for item in data['contents']:
            contents.append({
                'type': item['type'],
                'position': item['position'],
                'data': {
                    'content': item['data']['content'],
                    'url': item['data']['url'],
                }
            })

        post = Posts(
            title=data['title'],
            subtitle=data['subtitle'],
            cover_image=data['imageCover'],
            user_id=current_user.id,
            category=data['category'],
            source_name=data['source']['name'],
            source_url=data['source']['url']
        )

        database.session.add(post)
        database.session.commit()
        database.session.refresh(post)

        for content in contents:
            if content['type'] == 'IMG':
                image = Files.query.filter_by(
                    url=content['data']['content']).first()
                image.used = 1
            post_content = Post_Content(
                content=content['data']['content'],
                position=content['position'],
                type=content['type'],
                post_id=post.id,
            )
            database.session.add(post_content)
        cover_image = Files.query.filter_by(url=data['imageCover']).first()
        cover_image.used = 1
        database.session.commit()
        clearUploadCache()
        return jsonify({
            'status': 'success',
            'redirect': url_for('notice', id=post.id)
        })

    return render_template(
        'pages/posts/new_post.html',
        title='Nova postagem',
        selected='new',
        sub_header=sub_header(2, 'posts'),
    )


@app.route('/posts/edit/<int:id>')
@login_required
def edit_post(id):
    return 'Disponível em breve...'


@app.route('/posts/delete/<int:id>')
@login_required
def delete_post(id):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if current_user.is_admin != 1 and current_user.is_poster != 1:
        return redirect(url_for('index'))

    post = Posts.query.filter_by(id=id).first()
    posts_content = Post_Content.query.filter_by(post_id=id).all()

    for post_content in posts_content:
        if post_content.type == 'IMG':
            delete_file(post_content.content)
        database.session.delete(post_content)

    database.session.commit()
    delete_file(post.cover_image)

    database.session.delete(post)
    database.session.commit()

    return redirect(url_for('posts'))


@app.route('/get-site-informations', methods=['post'])
def getSiteInformations():
    data = json.loads(request.data)

    site_url = data['url']

    httpOrHttps = data['url'].split('//')[0]

    url = site_url.split(httpOrHttps + '//')
    url = url[1].split('/')
    url_origin = httpOrHttps + '//' + url[0]

    page = requests.get(url_origin)
    page = page.content

    soup = BeautifulSoup(page, 'html.parser')

    site_name = soup.find("meta",  property="og:site_name")['content']

    return jsonify({
        'site_name': site_name,
        'site_url_origin': url_origin,
    })
