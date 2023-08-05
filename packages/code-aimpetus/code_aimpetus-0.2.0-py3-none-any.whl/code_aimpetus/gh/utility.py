from github import Github
from github.Repository import Repository


def get_repo(token: str, owner: str, repo: str) -> Repository:
    """Get a GitHub repository object.

    Args:
        token (str): GitHub access token.
        owner (str): Repository owner.
        repo (str): Repository name.

    Returns:
        github.Repository.Repository: A GitHub repository object."""
    g = Github(token)
    return g.get_repo(f"{owner}/{repo}")
