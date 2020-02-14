from flask_frozen import Freezer
from simplertimes import create_app

if __name__ == '__main__':

    import warnings
    from flask_frozen import MissingURLGeneratorWarning, MimetypeMismatchWarning
    # This supress warnings of this kind:
    # MissingURLGeneratorWarning: Nothing frozen for endpoints admin. Did you forget a URL generator?
    warnings.simplefilter('ignore' , MissingURLGeneratorWarning)

    # This supress warnings of this kind: 
    # MimetypeMismatchWarning: Filename extension of 'admin' (type application/octet-stream) does not match Content-Type: text/html; charset=utf-8
    warnings.simplefilter('ignore' , MimetypeMismatchWarning)

    freezer = Freezer(create_app())
    freezer.freeze()