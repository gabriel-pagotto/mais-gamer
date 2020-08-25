from app import database


class Games(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(30), unique=True)

    def __repr__(self):
        return '<Games {}>'.format(self.name)

class Games_Relations(database.Model):
  id = database.Column(database.Integer, primary_key=True)
  game = database.Column(database.Integer, database.ForeignKey('games.id'))
  post = database.Column(database.Integer, database.ForeignKey('posts.id'))

  def __repr__(self):
    return '<Games_Relations>'.format(self.game)
