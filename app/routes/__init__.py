from app import app
from app.routes import auth, posts, files


from app.utils.date_time import DatePost
from app.utils.database_models import post_categories


@app.context_processor
def global_functions():
    return dict(
        DatePost=DatePost,
        post_categories=post_categories(),
    )
