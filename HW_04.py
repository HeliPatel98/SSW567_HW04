import requests
import json

def get_repo(user_name = 'HeliPatel98'):
    output = []
    url = 'https://api.github.com/users/{}/repos'.format(user_name)
    resq = requests.get(url)
    repos = json.loads(resq.text)
    output.append('User: {}'.format(user_name))

    try:
        repos[0]['name']
    except(TypeError, KeyError, IndexError):
        return 'unable to fetch repository'

    try:
        for repo in repos:
            repo_name = repo['name']
            repo_url = 'https://api.github.com/repos/{}/{}/commits'.format(user_name, repo_name)
            repo_info = requests.get(repo_url)
            repo_info_json = json.loads(repo_info.text)
            output.append('Repository: {} Number of commits: {}'.format(repo_name,len(repo_info_json)))
    except(TypeError, KeyError, IndexError):
        return 'unable to fetch commits'
    return output

if __name__ == '__main__':
    for ex in get_repo():
        print(ex)


