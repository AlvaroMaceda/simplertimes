from flask import Flask, render_template

def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config')
    
    @app.route('/admin')
    def admin():
        return app.config["BANANA"]

    @app.route('/')
    def root():
        from simplertimes.posts.post import Post
        from simplertimes.posts.posts_repository import PostsRepository
        return render_template('/index.html')

    return app