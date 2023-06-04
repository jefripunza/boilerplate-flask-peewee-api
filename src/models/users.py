import datetime

from peewee import *
from src.utils.database import BaseModel, database

from hashlib import md5

# the user model specifies its fields (or columns) declaratively, like django
class Users(BaseModel):
    id = AutoField()
    name = CharField(null=False)
    username = CharField(null=False, index=True, unique=True)
    password = CharField(null=False)
    join_date = DateTimeField(default=datetime.datetime.now)
    role = CharField(null=False)

    def is_username_exist(username):
        try:
            Users.get(
                (Users.username == username)
            )
            return True
        except:
            return False

    def new_user(name, username, password, role):
        password = md5((password).encode('utf-8')).hexdigest()
        try:
            Users \
                .create(
                    name=name,
                    username=username,
                    password=password,
                    role=role,
                )
            return True
        except Exception as e:
            print(e)
            return False

    def is_login(username, password):
        password = md5((password).encode('utf-8')).hexdigest()
        try:
            return Users \
                .select(Users.id, Users.role) \
                .where(
                    (Users.username == username) & (Users.password == password)
                ) \
                .first()
        except Exception as e:
            print(e)
            return False
