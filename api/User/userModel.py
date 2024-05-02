from peewee import *

class User(Model):
    id = AutoField(primary_key=True)
    name = CharField()
    email = CharField(unique=True)
    password = CharField()
    role = CharField()
