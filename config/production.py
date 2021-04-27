


from config.default import *

SQLALCHEMY_DATABASE_URI = 'sqllit:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = b'\xbc\x9eW\xb7\x15\xf9^\xf5\x99\xd3j\xd9\xfc)\xde\x97' 
