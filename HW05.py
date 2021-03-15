import requests

def list_repo(user_name):
    repo_url = requests.get("https://api.github.com/users/{}/repos".format(user_name))
    repo_list = [item['name'] for item in repo_url.json()]
    return repo_list

def commits(user_name,repo):
    repo_commit = requests.get("https://api.github.com/repos/{}/{}/commits".format(user_name,repo))
    commit_count = 0
    for _ in repo_commit.json():
        commit_count += 1
    return commit_count