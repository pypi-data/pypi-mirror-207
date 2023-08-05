from celery import Celery
import click


app = Celery(
    "tasks", broker="redis://localhost:6379/0", backend="redis://localhost:6379/0"
)


@click.command()
def start_app():
    app.start()
