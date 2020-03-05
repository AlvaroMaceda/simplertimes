from .post import Post

def value_of(field_names, row, field):
    try:
        return row[field_names.index(field)]
    except ValueError:
        return None

class PostFactory():
    
    @staticmethod
    def from_sqlite3_row(cursor, row):

        field = lambda x: value_of(field_names, row, x)
        
        field_names = list(map(lambda x:x[0], cursor.description))
    
        return Post(
            id = field('id'),
            friendly_name = field('friendly_name'),
            title = field('title'),
            date = field('creation_datetime'),
            content = field('content'),
            commit = field('commit'),
        )