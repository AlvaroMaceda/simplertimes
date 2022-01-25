from flask import Flask, g
from flask import render_template

from .db import get_db, close_db

def create_app(debug = False):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    app.debug = debug

    @app.after_request
    def after_request(response):
        close_db()
        return response

    @app.errorhandler(404)
    def page_not_found(e):
        return render_template('404.html'), 404

    @app.route('/post/<friendly_name>')
    def post(friendly_name):
        from simplertimes.posts import PostsRepository
        pr = PostsRepository(get_db())
        post = pr.by_friendly_name(friendly_name)
        if not post: return render_template('/404.html'),404
        return render_template('/standalone_post.html', post=post)

    @app.route('/admin/<_>')
    def admin(_=None):
        return 'pass'

    @app.route('/')
    def root():
        from simplertimes.posts import PostsRepository
        pr = PostsRepository(get_db())
        return render_template('/index.html', posts=pr.home_posts())

    return app
