# flask-dash-example
Deployment example for an app where the main part is a dash app with flask server managing several static and non-static pages as well

## Running

- create and activate virtual environment
- ```pip install -r requirements```

Running with gunicorn:
```
gunicorn -w 4 'app:server'
```
