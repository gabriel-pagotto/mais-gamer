from app import app
from app.models import Games
from app.utils.date_time import DatePost
from app.utils.header_games import header_games
from app.utils.limit_notices import limit_notices
from app.utils.main_page_posts_control import posts_control
from flask import render_template

@app.route('/', methods=['GET'])
def index():
    if not posts_control()[0] or len(posts_control()[0]) < 4:
        return render_template(
            'index.html',
            title = 'Mais Gamer - Notícias para Gamers',
            last_notices = None,
            DatePost = DatePost,
            header_games = header_games,
            limit_notices = limit_notices,
        )

    games = Games.query.order_by('name').all()

    return render_template(
        'index.html',
        title = 'Mais Gamer - Notícias sobre Games e eSports',
        last_notice = posts_control()[1],
        last_notices = posts_control()[2],
        rest_notices = posts_control()[3],
        games = games,
        DatePost = DatePost,
        header_games = header_games,
        limit_notices = limit_notices,
    )
