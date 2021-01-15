## Comic Media Server

The purpose of this project was to get acquainted with Django and managing my comic collection.

### Server
```bash
source ~/.virtualenvs/djangodev/bin/activate
python3 manage.py makemigrations server
python3 manage.py migrate
python3 manage.py runserver
```

### Redis
Redis is required for this project. Redis only needs to be ran if celery is being used.
```bash
redis-server
```

### celery
Celery is required to test the background test. Note that celery does not need to be running to start the server.
```bash
celery -A comiix worker -l info
```
