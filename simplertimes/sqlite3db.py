import sqlite3

class SQLite3DB():

    def __init__(self, db_path):
        self._db = None
        self.db_path = db_path

    def db(self):
        if not self._db:
            self._db = sqlite3.connect(
                self.db_path,
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            self._db.row_factory = sqlite3.Row

        return self._db

    def close(self):
        if self._db is not None:
            self._db.close()

    def query(self, query, args=(), one=False, factory=sqlite3.Row):
        
        self.db().row_factory = factory
        cur = self.db().execute(query, args)
        
        if one: 
            rv = c.fetchone()
            row = rv[0] if rv else None
        else:
            rv = cur.fetchall()
        cur.close()
        return row if one else rv