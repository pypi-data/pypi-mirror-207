import os

import click
from github import Github


@click.command()
@click.option(
    "--token",
    help="Your GitHub access token",
    default=os.environ.get("GITHUB_TOKEN", ""),
)
@click.option("--repo_name", help="The name of the new repository", required=True)
@click.option("--description", help="The description of the new repository", default="")
@click.option("--private", help="Set the repository to private", is_flag=True)
def create_github_repo(token, repo_name, description=None, private=False):
    g = Github(token)
    user = g.get_user()
    try:
        repo = user.create_repo(repo_name, description=description, private=private)
        print(f"Successfully created repository: {repo_name}")
        return repo
    except Exception as e:
        print(f"Error creating repository: {e}")
        return None
