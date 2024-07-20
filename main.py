from github import Github

# Authentication is defined via github.Auth
from github import Auth
from git import Repo
import subprocess
import shutil
import os
from progress_bar import GitRemoteProgress

# using an access token
auth = Auth.Token(os.getenv("GITHUB_TOKEN"))

# Public Web Github
g = Github(auth=auth)

# Then for each repo that you have access to:
for repo in g.get_user().get_repos():
    txtfile_exists = os.path.exists("output") and repo.name in map(
        lambda x: x.split(".txt")[0],
        filter(lambda x: x.endswith(".txt"), os.listdir("output")),
    )
    if txtfile_exists:
        continue
    print("Cloning " + repo.ssh_url)
    clone = Repo.clone_from(
        repo.ssh_url,
        "output/" + repo.name,
        progress=GitRemoteProgress(),
    )
    print("Bundling " + repo.name + " to " + repo.name + ".bundle")
    subprocess.run(
        f"cd output/{repo.name} && git bundle create ../{repo.name}.bundle --all",
        shell=True,
    )
    print("Generating log for " + repo.name)
    subprocess.run(
        f"cd output/{repo.name} && git log --pretty=format:'%h %s' > ../{repo.name}.txt",
        shell=True,
    )
    print("Removing cloned repo " + repo.name)
    shutil.rmtree(f"output/{repo.name}", ignore_errors=True)


# To close connections after use
g.close()
