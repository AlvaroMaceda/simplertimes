from simplertimes import create_app
from livereload import Server, shell

def make_livereload_server(wsgi_app):
    server = Server(wsgi_app)

    watch_patterns = (
        "simplertimes/**",
        "/home/alvaro/Software/simplertimes_environment/src/simplertimes/__init__.py"
    )

    for pattern in watch_patterns:
        server.watch(pattern,shell('ls -la'))

    return server

if __name__ == '__main__':
    # app = create_app()
    # app.run(debug=True)

    flask_wsgi_app = create_app().wsgi_app
    server = make_livereload_server(flask_wsgi_app)
    server.serve()
