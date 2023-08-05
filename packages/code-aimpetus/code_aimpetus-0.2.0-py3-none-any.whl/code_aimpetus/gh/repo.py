import click
from common_options import apply_github_token
from github import Github
from loguru import logger


@click.command()
@apply_github_token
@click.option("--repo_name", help="The name of the new repository", required=True)
@click.option("--description", help="The description of the new repository", default="")
@click.option("--private", help="Set the repository to private", is_flag=True)
def create_github_repo(token, repo_name, description=None, private=False):
    """
    Create a new GitHub repository

    Args:
        token (str): GitHub access token
        repo_name (str): The name of the new repository
        description (str): The description of the new repository
        private (bool): Set the repository to private

    Returns:
        github.Repository.Repository: A GitHub repository object."""
    g = Github(token)
    user = g.get_user()
    try:
        repo = user.create_repo(repo_name, description=description, private=private)
        logger.info(f"Successfully created repository: {repo}")
        return repo
    except Exception as e:
        logger.info(f"Error creating repository: {e}")
        return None
