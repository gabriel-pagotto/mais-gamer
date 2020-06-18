from flask import render_template
from app.forms import SearchForm

@app.route('/search', methods=['GET'])
def search():
    form = SearchForm

    return render_template(
        'notices.html',
        title = 'search_value',
        form = form,
    )
