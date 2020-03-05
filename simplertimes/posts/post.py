import datetime

def banana():
    return 'banana'

class Post():

    def __init__(self, id='', friendly_name='', title = '', content = '', date = datetime.datetime.now(), commit=None):
        self.id = id
        self.friendly_name = friendly_name
        self.title = title
        self.content = content
        self.date = date
        self.commit = commit
    
