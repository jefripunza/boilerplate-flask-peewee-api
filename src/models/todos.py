import datetime

from peewee import *
from src.modules.database import BaseModel

from src.models import Users

# a dead simple one-to-many todos: one user has 0..n todos, exposed by
# the foreign key. because we didn't specify, a users messages will be accessible
class Todos(BaseModel):
    id = AutoField()
    user_id = ForeignKeyField(Users, backref='todos')
    content = TextField()
    pub_date = DateTimeField(default=datetime.datetime.now)
    is_done = BooleanField(default=False)

    def new(content, user_id):
        try:
            Todos.create(
                content=content,
                user_id=user_id,
            )
            return True
        except Exception as e:
            print(e)
            return False

    def list_by_user_id(user_id):
        res = Todos \
            .select(Todos.id, Todos.content, Todos.is_done, Todos.pub_date) \
            .where(Todos.user_id == user_id).dicts()
        return list(res)

    def is_exist(id, user_id):
        try:
            return Todos.get(
                (Todos.id == id) & (Todos.user_id == user_id)
            )
        except:
            return False

    def update_by_id(id, user_id, content):
        try:
            Todos.update(
                    content=content,
                ).where(
                    (Todos.id == id) & (Todos.user_id == user_id)
                ).execute()
            return True
        except Exception as e:
            print(e)
            return False

    def delete_by_id(id, user_id):
        try:
            Todos.delete() \
                .where(
                    (Todos.id == id) & (Todos.user_id == user_id)
                ).execute()
            return True
        except Exception as e:
            print(e)
            return False

    def done_by_id(id, user_id, is_done):
        try:
            Todos.update(
                    is_done=is_done,
                ).where(
                    (Todos.id == id) & (Todos.user_id == user_id)
                ).execute()
            return True
        except Exception as e:
            print(e)
            return False
