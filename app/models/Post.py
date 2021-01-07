from app import database
from app.utils.date_time import datetime_sao_paulo


class Posts(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    title = database.Column(database.String(300))
    subtitle = database.Column(database.String(450))
    cover_image = database.Column(database.Text)
    user_id = database.Column(
        database.Integer, database.ForeignKey('users.id'))
    category = database.Column(
        database.Integer, database.ForeignKey('categories.id'))
    created_at = database.Column(database.DateTime, default=datetime_sao_paulo)
    views = database.Column(database.Integer, default=0)
    source_name = database.Column(database.String(50))
    source_url = database.Column(database.Text)

    def __repr__(self):
        return '<Posts {}>'.format(self.posts)


class PostContents(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    content = database.Column(database.Text)
    position = database.Column(database.Integer)
    type = database.Column(database.String(3))
    post_id = database.Column(
        database.Integer, database.ForeignKey('posts.id'))

    def __repr__(self):
        return '<Post_Content>'.format(self.post_content)


class Categories(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(20))

    def __repr__(self):
        return '<PostCategory>'.format(self.name)
