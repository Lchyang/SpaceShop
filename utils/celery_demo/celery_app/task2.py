import time
from celery_app import app


@app.task
def multiply(x, y):
    print("enter multiply function...")
    time.sleep(5)
    return x * y
