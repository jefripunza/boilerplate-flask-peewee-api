# Python Microservice - Flask (Peewee)

## Features
- Auto Import Controller (duplicate index.py to your controller, change Blueprint name, custom endpoint and happy code...)
- JWT On The Go! (with token management)
- Use Peewee ORM (in NodeJS like Knex)
- Auto Migration Table on Models (only change your model)
- Docker Ready!
- Swagger Auto Generate

## How to Use
- install dependencies `python -m pip install -r requirements.txt`
- generate swagger : `python -m flask spec`
- run : `python -m flask --app main run`
- run dev : `python -m flask --app main run --debug`

## You Can Use Scripts
#### Remove all __pycache__ directory
```bash
find . | grep -E "(__pycache__|\.pyc$)" | xargs rm -rf
```