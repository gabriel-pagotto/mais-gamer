import random
from app import app, database
from app.models import Users, Posts, Post_Content
from app.utils.date_time import get_datetime_7_days
from flask import render_template, redirect, request, url_for
from sqlalchemy import desc


@app.route('/news/<id>', methods=['GET'])
def notice(id):
    all_posts = Posts.query.all()
    all_posts_array = []
    for post in all_posts:
        if post.id != id and get_datetime_7_days(post.addedAt) == True:
            all_posts_array.append(post)

    num_randons = []
    more_news = []
    try:
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

        for num in num_randons:
            more_news.append(all_posts_array[num])

    except ValueError:
        more_news = None

    post = Posts.query.filter_by(id=id).first()
    post_content = Post_Content.query.filter_by(
        post_id=id).order_by('position')
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
        more_news=more_news,
    )


@app.route('/notícia/<id>', methods=['GET'])
def notice_redirect(id):
    return redirect(url_for('notice', id=id))
