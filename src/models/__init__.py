import peeweedbevolve
from src.modules.database import database, _is_sqlite

from src.models.users import (Users)
from src.models.todos import (Todos)

# simple utility function to create tables
def create_tables():
    with database:
        if _is_sqlite:
            database.create_tables([Users, Todos], safe=True)
        else:
            database.evolve(interactive=False) # call this instead of db.create_tables
