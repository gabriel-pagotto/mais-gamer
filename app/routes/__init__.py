from app import app
from app.routes import index, admin, ajax, auth, notices, posts, user, search, files


from app.utils.date_time import DatePost
from app.utils.header import games, plataforms


@app.context_processor
def global_functions():
    return dict(
        DatePost=DatePost,
        games=games(),
        plataforms=plataforms(),
    )
