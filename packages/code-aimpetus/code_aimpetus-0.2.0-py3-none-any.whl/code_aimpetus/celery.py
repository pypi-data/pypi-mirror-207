import click
from celery import Celery

from code_aimpetus.settings import BROKER_URL

# Initialize Celery with Redis as the broker

app = Celery("codeai", broker=BROKER_URL, backend=BROKER_URL)


@click.command()
def start_app():
    app.start()
