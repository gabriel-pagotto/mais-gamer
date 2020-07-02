import os, json
from app import app, database
from app.models import Posts, Games, Post_Content
from app.forms import NewPostForm
from app.utils.aws_s3 import save_image_and_get_url, delete_image
from app.utils.header_games import header_games
from app.utils.sub_header_options import sub_header
from app.utils.url_for_notices import url_for_notices
from app.utils.date_time import DatePost
from flask import render_template, redirect, flash, request, url_for
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
    posts = Posts.query.filter_by(user_id = current_user.id).order_by(desc('addedAt')).paginate(page, 9, True)

    next_url = url_for('posts', page=posts.next_num) \
        if posts.has_next else None
    prev_url = url_for('posts', page=posts.prev_num) \
        if posts.has_prev else None
    
    return render_template(
        'posts/posts.html',
        DatePost = DatePost,
        title = 'Postagens',
        selected = 'posts',
        header_games = header_games,
        sub_header = sub_header(1, 'posts'),
        posts = posts.items,
        posts_pages = posts,
        page_number = page,
        next_url = next_url,
        prev_url = prev_url,
        url_for_notices = url_for_notices,
        last_param = None,
    )

@app.route('/posts/new', methods=['GET', 'POST'])
@login_required
def post_new():
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if current_user.is_admin != 1 and current_user.is_poster != 1:
        return redirect(url_for('index'))
    form = NewPostForm()
    games = Games.query.all()
    games_choices = [
        ('', 'Selecione uma opção'),
    ]
    for game in games:
        games_choices.append((game.id, game.name))
    form.game_id.choices = games_choices
    if form.submit():
        if request.method == 'POST':
            cover_image_url = save_image_and_get_url(request.files[form.cover_image.data.name])
            post = Posts(
                title = form.title.data,
                subtitle = form.subtitle.data,
                cover_image = cover_image_url,
                game_id = form.game_id.data,
                user_id = current_user.id,
            )

            database.session.add(post)
            database.session.commit()
            database.session.refresh(post)

            def add_content_database(content, position, type, post_id):
                post_content = Post_Content(
                    content = content,
                    position = position,
                    type = type,
                    post_id = post_id,
                )
                return database.session.add(post_content)

            pc_image = save_image_and_get_url(request.files[form.pc_image.data.name])
            pc_last_image = save_image_and_get_url(request.files[form.pc_last_image.data.name])
            add_content_database(pc_image, 1, 'IMG', post.id)
            add_content_database(form.pc_text.data, 2, 'TXT', post.id)
            add_content_database(pc_last_image, 3, 'IMG', post.id)
            add_content_database(form.pc_last_text.data, 4, 'TXT', post.id)
            
            database.session.commit()

            return redirect(url_for('notice', id=post.id))

    return render_template(
        'posts/posts.html',
        title = 'Nova postagem',
        selected = 'new',
        form = form,
        choices = games_choices,
        header_games = header_games,
        sub_header = sub_header(2, 'posts'),
    )

@app.route('/posts/delete/<int:id>')
@login_required
def delete_post(id):
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if current_user.is_admin != 1 and current_user.is_poster != 1:
        return redirect(url_for('index'))

    post = Posts.query.filter_by(id = id).first()
    posts_content = Post_Content.query.filter_by(post_id = id).all()
    

    for post_content in posts_content:
        if post_content.type == 'IMG':
            delete_image(post_content.content)
        database.session.delete(post_content)
    
    delete_image(post.cover_image)
    
    database.session.delete(post)
    database.session.commit()

    return redirect(url_for('posts'))
