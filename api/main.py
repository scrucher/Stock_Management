
from .Config import index
from User import userModel as User
port = 8080

def __main__():

    db=index.db
    try:
        db.connect()
        db.create_tables([User,])
        print('Server Started'),
    except(Exception) as e:
        print(e)
