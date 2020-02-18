import datetime

def banana():
    return 'banana'

class Post():

    def __init__(self, title = '', content = '', date = datetime.datetime.now(), commit=None):
        self.title = title
        self.content = content
        self.date = date
        self.commit = commit
    
