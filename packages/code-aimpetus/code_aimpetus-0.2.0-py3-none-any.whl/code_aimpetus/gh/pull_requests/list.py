import click
from gh.utility import get_repo
from github.PaginatedList import PaginatedList
from github.PullRequest import PullRequest
from loguru import logger

from code_aimpetus.common_options import apply_github_options


@click.command()
@apply_github_options
def list_pull_requests(token, owner, repo) -> PaginatedList[PullRequest]:
    """
    List all pull requests for a given repository

    Args:
        token (str): GitHub access token.
        owner (str): Repository owner.
        repo (str): Repository name.

    Returns:
        github.PaginatedList.PaginatedList[github.PullRequest.PullRequest]:
            A list of GitHub pull request objects.
    """
    repo = get_repo(token, owner, repo)
    pull_requests = repo.get_pulls(state="open")
    for pr in pull_requests:
        logger.info(f"#{pr.number}: {pr.title}")
    return pull_requests
