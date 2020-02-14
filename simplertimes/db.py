from flask import current_app, g
from simplertimes.sqlite3db import SQLite3DB

def get_db():
    if 'db' not in g:
        g.db = SQLite3DB(current_app.config['DATABASE'])
    return g.db   

def close_db():
    db = g.pop('db', None)
    if db is not None:
        db.close()