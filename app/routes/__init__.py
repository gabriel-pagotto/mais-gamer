from app import app
from app.routes import index, admin, auth, notices, posts, user, search, files


from app.utils.date_time import DatePost


@app.context_processor
def global_functions():
    return dict(
        DatePost=DatePost,
    )
