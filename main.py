from dotenv import load_dotenv
load_dotenv()

from src import app
from src.models import create_tables

from config import PORT

if __name__ == "main":
    create_tables()
    print("Starting server at %s..." % PORT)
    app.run()
