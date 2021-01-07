from app.models import Categories


def post_categories():
    return Categories.query.order_by('id').all()
