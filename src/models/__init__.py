import peeweedbevolve # don't delete this...
from src.modules.database import database, _is_sqlite

from src.models.users import (Users)
from src.models.todos import (Todos)
from src.models.products import (ProductCategories)

# simple utility function to create tables
def create_tables():
    with database:
        try:
            if _is_sqlite:
                database.create_tables([
                    Users,
                    Todos,
                    ProductCategories,
                ], safe=True)
            else:
                database.evolve(interactive=False) # call this instead of db.create_tables
        except:
            # os.execl(sys.executable, os.path.abspath(__file__), *sys.argv) # restart by code
            print("please run again your app...")
            exit()