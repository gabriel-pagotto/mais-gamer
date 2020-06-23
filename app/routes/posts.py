import os, json
from app import app, database
from app.models import Posts, Games, Post_Content
from app.forms import NewPostForm
from app.utils.aws_s3 import save_image_and_get_url
from app.utils.header_games import header_games
from flask import render_template, redirect, flash, request, url_for
from flask_login import current_user, login_required

def sub_header_posts(option_number):
    sub_header_options = {
        1: {
            'title': 'MINHAS POSTAGENS',
            'url': 'posts',
            'selected': False,
        },
        2: {
            'title': 'NOVA POAGEM',
            'url': 'posts_new',
            'selected': False,
        },
    }

    sub_header_options[option_number]['selected'] = True
    options = []
    counter = 1
    while counter < len(sub_header_options) + 1:
        options.append(sub_header_options[counter])
        counter = counter + 1
    return options

@app.route('/posts', methods=['GET'])
@login_required
def posts():
    post_options = []
    for option in sub_header_posts(1):
        post_options.append(option)
    if not current_user.is_authenticated:
        return redirect(url_for('login'))
    if current_user.is_admin != 1 and current_user.is_poster != 1:
        return redirect(url_for('index'))
    
    return render_template(
        'posts/posts.html',
        title = 'Postagens',
        selected = 'posts',
        header_games = header_games,
        sub_header = sub_header_posts(1),
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
        (0, 'Nenhum'),
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
        sub_header = sub_header_posts(2),
    )
