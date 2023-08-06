# Racoon

_View on [PyPI](https://pypi.org/project/py-racoon)_

## What is it?

A Python3 template initializer based on [nymann/python-template](https://github.com/nymann/python-template). That automatically sets up a GitHub project for you.

Example of generated project: [nymann/racoon-example](https://github.com/nymann/racoon-example)

## Installation

```sh
pip install py-racoon
```

## Usage

```sh
$ racoon --help
Usage: racoon [OPTIONS] URL

Arguments:
  URL  [required]

Options:
  --access-token PATH             [env var: GITHUB_ACCESS_TOKEN; default: /home/knj/.cache/github_token]
  --src-dir TEXT                  [default: src]
  --template-url TEXT             [default: https://github.com/nymann/python-template.git]
  --help                          Show this message and exit.
```

### Example

```sh
# Export your github access token file as an environment variable, can also be provided via --github-access-token
export GITHUB_ACCESS_TOKEN='YOUR_ACCESS_TOKEN'

# Create a new project "my-project" which will be created under https://github.com/YOUR_USERNAME/my-project
racoon my-project
```

## Development

For help getting started developing check [DEVELOPMENT.md](DEVELOPMENT.md)
