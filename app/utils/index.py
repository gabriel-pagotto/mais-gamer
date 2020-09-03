from flask import url_for


def return_url_category(category_id):
    if category_id == 1:
        return url_for('gaming_news')
    if category_id == 2:
        return url_for('e_sports')
    if category_id == 3:
        return url_for('trailer')
    if category_id == 4:
        return url_for('stream')
