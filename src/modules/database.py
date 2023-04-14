from peewee import *

from config import DATABASE_URL, DATABASE_DEBUG, \
    DATABASE_TYPE, DATABASE_HOST, DATABASE_PORT, \
    DATABASE_USER, DATABASE_PASS, DATABASE_NAME

import logging

if DATABASE_DEBUG:
    logger = logging.getLogger('peewee')
    logger.addHandler(logging.StreamHandler())
    logger.setLevel(logging.DEBUG)

# create a peewee database instance -- our models will use this database to
# persist information
_is_sqlite = DATABASE_URL.split(":///")[1] or False if DATABASE_URL.startswith("sqlite") else False
_is_mysql = DATABASE_URL if DATABASE_URL.startswith("mysql") else DATABASE_TYPE == 'mysql'
_is_postgres = DATABASE_URL if DATABASE_URL.startswith("postgres") else DATABASE_TYPE == 'postgres'

database = SqliteDatabase(_is_sqlite) if _is_sqlite \
    else MySQLDatabase(
        DATABASE_NAME,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        user=DATABASE_USER,
        password=DATABASE_PASS,
    ) if _is_mysql \
    else PostgresqlDatabase(
        DATABASE_NAME,
        host=DATABASE_HOST,
        port=DATABASE_PORT,
        user=DATABASE_USER,
        password=DATABASE_PASS,
    ) if _is_postgres \
    else SqliteDatabase('test.db')

# model definitions -- the standard "pattern" is to define a base model class
# that specifies which database to use.  then, any subclasses will automatically
# use the correct storage. for more information, see:
# https://charlesleifer.com/docs/peewee/peewee/models.html#model-api-smells-like-django
class BaseModel(Model):
    class Meta:
        database = database
