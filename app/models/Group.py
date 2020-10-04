from app import database
from app.utils.date_time import datetime_sao_paulo


class Groups(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.Text)
    description = database.Column(database.Text)
    icon = database.Column(database.Text)
    user_id = database.Column(
        database.Integer, database.ForeignKey('users.id'))
    createdAt = database.Column(database.DateTime, default=datetime_sao_paulo)
    confirmed = database.Column(database.Boolean, default=False)
    views = database.Column(database.Integer, default=0)

    def __repr__(self):
        return '<Groups {}>'.format(self.name)
