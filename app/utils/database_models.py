from app.models import PostCategory


def post_categories():
    return PostCategory.query.order_by('id').all()
