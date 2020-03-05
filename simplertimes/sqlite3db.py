import sqlite3

class SQLite3DB():

    def __init__(self, db_path):
        self.__db_conn = None
        self.__db_path = db_path

    def __db(self):
        if not self.__db_conn:
            self.__db_conn = sqlite3.connect(
                self.__db_path,
                detect_types=sqlite3.PARSE_DECLTYPES
            )
            self.__db_conn.row_factory = sqlite3.Row

        return self.__db_conn

    def close(self):
        if self.__db_conn is not None:
            self.__db_conn.close()

    def query(self, query, args_array=[], one=False, factory=sqlite3.Row):
    
        self.__db().row_factory = factory
        cur = self.__db().execute(query, tuple(args_array))
        
        if one: 
            row = cur.fetchone()
        else:
            rv = cur.fetchall()
        cur.close()
        return row if one else rv