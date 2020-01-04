import datetime

def banana():
    return 'banana'

class Post():

    def __init__(self, title = '', contents = '', date = datetime.datetime.now()):
        self.title = title
        self.contents = contents
        self.date = date