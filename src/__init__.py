import os
import sys

from flask import g, jsonify
from apiflask import APIFlask

from config import public_folder, SECRET_KEY
from src.modules.database import database

app = APIFlask(
    __name__,
    instance_relative_config=True,
    static_url_path='/public',
    static_folder=public_folder,
    title='Microservice API',
    version='1.0',
)
app.config.from_mapping(
    SECRET_KEY=SECRET_KEY,
)
app.config['SPEC_FORMAT'] = 'yaml'
app.config['LOCAL_SPEC_PATH'] = 'swagger.yaml'
app.config['LOCAL_SPEC_JSON_INDENT'] = 4
app.config['SYNC_LOCAL_SPEC'] = True

# Request handlers -- these two hooks are provided by flask and we will use them
# to create and tear down a database connection on each request.
@app.before_request
def before_request():
    g.db = database
    g.db.connect()

@app.after_request
def after_request(response):
    g.db.close()
    return response

@app.errorhandler(400)
def not_found(e):
    message = str(e)
    if message.endswith("request Content-Type was not 'application/json'."):
        return jsonify(
            message="body require!",
        ), 400
    return jsonify(
        message= message,
    ), 400

@app.errorhandler(404)
def not_found(e):
    return jsonify({'message' : 'Endpoint Not Found'}), 404

@app.errorhandler(500)
def internal_server_error(e):
    return jsonify({'message' : 'Internal Server Error'}), 500

# Controller Auto Import
controller_dir = os.path.join(os.path.dirname(__file__), 'controllers')
sys.path.insert(0, controller_dir)
for filename in os.listdir(controller_dir):
    if (filename[-3:].lower() == ".py" and not filename.startswith("#")):
        controller = __import__(os.path.basename(filename)[:-3])
        print("Generating", filename, controller)
        app.register_blueprint(controller.router)
sys.path.pop(0)
