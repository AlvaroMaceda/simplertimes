from flask import Flask, g
from flask import render_template

from .db import get_db, close_db

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')

    @app.after_request
    def after_request(response):
        close_db()
        return response     

    @app.route('/admin/<_>')
    def admin(_=None):
        return 'pass'

    @app.route('/')
    def root():
        from simplertimes.posts import PostsRepository
        pr = PostsRepository(get_db())
        return render_template('/index.html', posts=pr.home_posts())

    return app