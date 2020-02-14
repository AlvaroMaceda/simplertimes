import sqlite3
from .post_factory import PostFactory

class PostsRepository():

    def __init__(self, database):
        self.db = database

    def home_posts(self):
        cursor = self.db.query(
            '''
            SELECT * FROM Posts
            ORDER BY date(Posts.creation_datetime) desc
            '''
            ,factory = PostFactory.from_sqlite3_row)

        return cursor