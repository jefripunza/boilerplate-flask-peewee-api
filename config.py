import os

public_folder = os.path.join(os.path.dirname(__file__), 'public')

# ==================================================================================================================== #

# config - aside from our database, the rest is for use by Flask
PORT = int(os.environ.get('FLASK_RUN_PORT', 5000))
SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-secret-key-server'

# JWT
JWT_SECRET = os.environ.get('JWT_SECRET') or 's3cr3t'
JWT_EXPIRED_SECOND = eval(os.environ.get('JWT_EXPIRED_SECOND', "60"))
JWT_REFRESH_SECOND = eval(os.environ.get('JWT_REFRESH_SECOND', "30"))

# DATABASE
DATABASE_URL = os.environ.get('DATABASE_URL') or ''
DATABASE_TYPE = os.environ.get('DATABASE_TYPE') or 'mysql'
DATABASE_HOST = os.environ.get('DATABASE_HOST') or 'localhost'
DATABASE_PORT = int(os.environ.get('DATABASE_PORT', 3306))
DATABASE_USER = os.environ.get('DATABASE_USER') or 'root'
DATABASE_PASS = os.environ.get('DATABASE_PASS') or ''
DATABASE_NAME = os.environ.get('DATABASE_NAME') or 'microservice'
DATABASE_DEBUG = os.environ.get('DATABASE_DEBUG') == 'true' if os.environ.get('DATABASE_DEBUG') else False

# ==================================================================================================================== #

AUTH_SERVICE = os.environ.get('AUTH_SERVICE')

# ==================================================================================================================== #

role_register = ['buyer', 'merchant']
