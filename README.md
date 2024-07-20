# py-go-gitter

Helps backup your github repos to a bundle using `git bundle`, that can be used as a backup to restore from. For each repo, it creates a bundle file and a txt file containing formatted git-log output.

## Install

In your virtual environment, install the requirements.

```bash
pip install -r requirements.pip
```

## Usage

Generate Classic Access token from github. Your ssh key must be added to your github account else the clone will fail.

>**PS: If you want org repos, admin:org scope is required.

```bash
export GITHUB_TOKEN=your_github_token
```

```bash
python main.py
```

## Bonus

A shell script to download org repos to a folder
