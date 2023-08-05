import os

import click
from celery import Celery
from dotenv import load_dotenv

load_dotenv()

# Initialize Celery with Redis as the broker
broker_url = os.getenv("CELERY_BROKER_URL", "redis://:codeai@redis:6379/0")

app = Celery("codeai", broker=broker_url, backend=broker_url)


@click.command()
def start_app():
    app.start()
