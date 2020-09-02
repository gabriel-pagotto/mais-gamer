from app import app
from flask import request, jsonify
from app.models import Posts


@app.route('/buscar', methods=['GET'])
def search():
    def search(param):
        all_news = Posts.query.all()
        data_in_list = param.split(' ')
        list_news = []
        for news in all_news:
            list_news.append(news)
        news_selected = []
        for part in data_in_list:
            if part == '' and part == ' ' and part == None:
                return
            else:
                for news in list_news:
                    news_title = news.title.split(' ')
                    news_subtitle = news.subtitle.split(' ')
                    for title_word in news_title:
                        if part.lower() == title_word.lower():
                            news_selected.append(news)
                            break
                        for subtitle_word in news_subtitle:
                            if part.lower() == subtitle_word.lower():
                                news_selected.append(news)
                                break
                            break
        return news_selected

    q = request.args.get('q')

    results = []

    if q != None:
        data = search(q)
        if data == None:
            data = None
        elif len(data) < 1:
            data = None
        else:
            for result in data:
                results.append({
                    'id': result.id,
                    'title': result.title,
                    'subtitle': result.subtitle,
                    'cover_image': result.cover_image,
                    'user_id': result.user_id,
                    'addedAt': result.addedAt,
                    'views': result.views,
                    'source_name': result.source_name,
                    'source_url': result.source_url,
                })
    else:
        data = None

    return jsonify(results)
