from app import database

class Plataforms(database.Model):
  id = database.Column(database.Integer, primary_key=True)
  name = database.Column(database.String(30), unique=True)

  def __repr__(self):
    return '<Plataforms {}'.format(self.name)

class Plataforms_Relations(database.Model):
  id = database.Column(database.Integer, primary_key=True)
  plataform = database.Column(database.Integer, database.ForeignKey('plataforms.id'))
  post = database.Column(database.Integer, database.ForeignKey('posts.id'))

  def __repr__(self):
    return '<Plataform_Relations>'.format(self.plataform)
