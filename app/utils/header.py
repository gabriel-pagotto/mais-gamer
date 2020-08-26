from app.models import Games, Plataforms

def games():
  return Games.query.order_by('name').all()

def plataforms():
  return Plataforms.query.order_by('name').all()
