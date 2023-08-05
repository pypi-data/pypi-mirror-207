import click
from .celery import start_app

from code_aimpetus.gh.issues.close import close_issue
from code_aimpetus.gh.issues.list import list_issues
from code_aimpetus.gh.pull_requests.list import list_pull_requests
from code_aimpetus.gh.repo import create_github_repo


@click.group()
def cli():
    pass


cli.add_command(list_pull_requests)
cli.add_command(list_issues)
cli.add_command(close_issue)
cli.add_command(create_github_repo)
cli.add_command(start_app)

if __name__ == "__main__":
    cli()
