import time
from celery_app import app


@app.task
def add(x, y):
    print("enter add function...")
    time.sleep(5)
    return x + y
