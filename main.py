from dotenv import load_dotenv
load_dotenv()

from src import app
from src.models import create_tables
from src.swagger import auto_generate_swagger

from config import PORT

if __name__ == "__name__":
    create_tables()
    print("Starting server at %s..." % PORT)
    auto_generate_swagger()
    app.run(host='0.0.0.0')
