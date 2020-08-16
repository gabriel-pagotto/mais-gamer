from app import database


class Games(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(30), unique=True)
    icon = database.Column(database.Text)

    def __repr__(self):
        return '<Games {}>'.format(self.games)
