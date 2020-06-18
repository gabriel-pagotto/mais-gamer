from app import database
from datetime import datetime
from flask_login import UserMixin

class Posts(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(90))
    subtitle = database.Column(database.String(450))
    cover_image = database.Column(database.Text)
    game_id = database.Column(database.Integer, database.ForeignKey('games.id'))
    user_id = database.Column(database.Integer, database.ForeignKey('users.id'))
    addedAt = database.Column(database.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return '<Posts {}>'.format(self.posts)

class Post_Content(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    content = database.Column(database.Text)
    position = database.Column(database.Integer)
    type = database.Column(database.String(3))
    post_id = database.Column(database.Integer, database.ForeignKey('posts.id'))

    def __repr__(self):
        return '<Post_Content>'.format(self.post_content)
