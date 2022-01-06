# Projectile

A boilerplate for django 4.0.1 projects

## Requirements

- Python 3.9
- PostgreSQL
- Redis
- Docker

## How to run

### Normal Environment

- Install all Python 3.9
- Install PostgreSQL, Redis or Docker
- If docker then see how to **Run services using docker**
- Make a virtualenv and use it
- Install requirements `pip3 install -r requirements.txt`
- Run migrations `python3 manage.py migrate`
- Create an admin user `python3 manage.py createsuperuser`
- Run the server `python3 manage.py runserver`
- Go to [localhost:8000](http://localhost:8000)
- For django admin go to [localhost:8000/admin](http://localhost:8000/admin)

### Run services using docker

- Run `docker-compose up -d`
- To stop run `docker-compose down`

## Credits

- Mazhar Ahmed

> Copyright (c) Mazhar Ahmed
