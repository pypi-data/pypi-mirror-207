import click

from code_aimpetus.settings import GITHUB_OWNER, GITHUB_REPO, GITHUB_TOKEN

common_options = [
    click.option("--token", help="Your GitHub access token", default=GITHUB_TOKEN),
    click.option("--owner", help="Repository owner", default=GITHUB_OWNER),
    click.option("--repo", help="Repository name", default=GITHUB_REPO),
]


def apply_github_options(func):
    for option in reversed(common_options):
        func = option(func)
    return func


def apply_github_token(func):
    func = common_options[0](func)
    return func
