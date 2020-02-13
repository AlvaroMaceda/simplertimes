from flask import Flask, g
from flask import render_template
# import sqlite3
from simplertimes.db import get_db, close_db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')

    @app.after_request
    def after_request(response):
        close_db()
        return response     

    @app.route('/admin')
    def admin():
        return 'pass'

    @app.route('/test_db')
    def test_db():
        db = get_db()
        return 'foo'

    @app.route('/')
    def root():
        from simplertimes.posts.post import Post
        from simplertimes.posts.posts_repository import PostsRepository
        return render_template('/index.html')

    return app