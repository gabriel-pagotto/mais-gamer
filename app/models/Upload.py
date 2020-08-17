from app import database


class Image(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    url = database.Column(database.Text)

    def __repr__(self):
        return '<Image {}>'.format(self.games)
