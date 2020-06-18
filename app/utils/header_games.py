from app.models import Games

def games():
    return Games.query.order_by('name').all()

header_games = games()
