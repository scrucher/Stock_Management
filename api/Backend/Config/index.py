from pony.orm import *
db = Database()

def db_connection():
    try:
        db.bind(provider='mysql', host='localhost', user='root', passwd='', db='saley_stock')
        return db
    except Exception as e:
        return e