# flask-dash-example
Deployment example for an app where the main part is a dash app with flask server managing several static and non-static pages as well

## Running

- create and activate virtual environment
- ```pip install -r requirements```

Running with gunicorn:

```
gunicorn --bind 127.0.0.1:8005 --workers 4 'app.app:server'
```

## Deploy with Podman
Works similarily with Docker.

```
podman build -f deploy/Dockerfile --tag flask-dash-gunicorn:0.1 .
podman run --rm --name gunicorn-dash-gunicorn-container -p "8005:8005" -d flask-dash-gunicorn:0.1
```
