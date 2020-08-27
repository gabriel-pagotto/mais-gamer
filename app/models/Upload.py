from app import database


class Files(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    url = database.Column(database.Text)
    used = database.Column(database.Boolean, default=False)

    def __repr__(self):
        return '<Files {}>'.format(self.url)
