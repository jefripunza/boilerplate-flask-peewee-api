
from src import app
from config import IS_DEVELOPMENT
def auto_generate_swagger():
    # generate auto swagger
    if IS_DEVELOPMENT:
        app.spec
        print("Generating swagger.yaml")