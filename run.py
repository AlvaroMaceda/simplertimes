from simplertimes import create_app
from livereload import Server, shell

def make_livereload_server(wsgi_app):
    server = Server(wsgi_app)

    watch_patterns = (
        "simplertimes/**/*.*",
    )

    for pattern in watch_patterns:
        server.watch(pattern)

    return server

if __name__ == '__main__':
    flask_wsgi_app = create_app(debug=True).wsgi_app
    server = make_livereload_server(flask_wsgi_app)
    server.serve()
