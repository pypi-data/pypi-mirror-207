from pathlib import Path
import sys
import urllib.parse

from github import Github
from github.Repository import Repository
from github import UnknownObjectException
import typer

from racoon.argument_types import DefaultSrcDir
from racoon.argument_types import DefaultTemplateURL
from racoon.argument_types import RequiredAccessToken
from racoon.git import init_template
from racoon.github_integration import GitHubIntegration
from racoon.template_generation import Context
from racoon.template_generation import generate_template


class Repo:
    def __init__(self, group: str, name: str) -> None:
        self.group: str = group
        self.name: str = name

    @classmethod
    def from_url(cls, url: str) -> "Repo":
        parsed_url = urllib.parse.urlparse(url)
        path_components = parsed_url.path.rstrip("/").split("/")
        return cls(group=path_components[-2], name=path_components[-1])

    def to_url(self) -> str:
        return f"https://github.com/{self.group}/{self.name}"


app = typer.Typer()


def read_file(path: Path) -> str:
    with open(path, "r") as file_pointer:
        return file_pointer.read().strip("\n")


def get_full_name_from_url(url: str) -> str:
    interesting: str = url[url.index(".") :]
    parts: list[str] = interesting.split("/")[1:]
    return "/".join(parts)


def get_repo_by_url(url: str, github: Github) -> Repository:
    full_name = get_full_name_from_url(url=url)
    return github.get_repo(full_name_or_id=full_name)


def create_repo(url: str, github: Github) -> Repository:
    repo = Repo.from_url(url)
    user = github.get_user()
    if user.name == repo.group:
        return user.create_repo(name=repo.name)
    org = github.get_organization(repo.group)
    return org.create_repo(name=repo.name)


def get_or_create_repo(url: str, github: Github) -> Repository:
    try:
        return get_repo_by_url(url=url, github=github)
    except UnknownObjectException:
        typer.echo(f"The repository '{url}' does not exists. Creating it.")
        return create_repo(url=url, github=github)


@app.command()
def generate(
    url: str,
    access_token: Path = RequiredAccessToken,
    src_dir: str = DefaultSrcDir,
    template_url: str = DefaultTemplateURL,
) -> None:
    github = Github(login_or_token=read_file(path=access_token))
    repo: Repository = get_or_create_repo(github=github, url=url)
    user = github.get_user()
    context = Context(
        name=user.name,
        email=user.email,
        url=url,
        src_dir=src_dir,
        full_name=get_full_name_from_url(url=url),
    )
    generate_template(template_url=template_url, context=context)
    github_integration = GitHubIntegration(github=github)
    repo = github_integration.setup(repo=repo)
    init_template(repository=repo)


if __name__ == "__main__":
    app()
