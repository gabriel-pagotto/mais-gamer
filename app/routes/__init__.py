from app import app
from app.routes import admin, ajax, auth, cover, notices, posts, user, search, files


from app.utils.header_games import header_games
from app.utils.date_time import DatePost


@app.context_processor
def global_functions():
    return dict(
      header_games = header_games,
      DatePost = DatePost,
    )
