#!/bin/bash

rm -rf oneleftfootapi/migrations
rm db.sqlite3
python3 manage.py makemigrations oneleftfootapi
python3 manage.py migrate
python3 manage.py loaddata users
python3 manage.py loaddata tokens
python3 manage.py loaddata dance_users
python3 manage.py loaddata partners
python3 manage.py loaddata dance_types
python3 manage.py loaddata skill_levels
python3 manage.py loaddata roles
python3 manage.py loaddata dance_type_join
python3 manage.py loaddata days
python3 manage.py loaddata availability
python3 manage.py loaddata requests


# heroku run python3 manage.py loaddata