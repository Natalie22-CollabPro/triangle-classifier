# Natalie Aragon 
# Assignment 3a - Github API
#02/28/2026 

import requests

def get_repo_commit_counts(username):
    # Get all repos for the user
    repos_url = f"https://api.github.com/users/{username}/repos"
    repos_response = requests.get(repos_url, timeout=10)

    if repos_response.status_code != 200:
        return f"Error: User not found or request failed ({repos_response.status_code})"

    repos = repos_response.json() 
    results = []

    for repo in repos:
        repo_name = repo["name"]

        # Get commits for each repo
        commits_url = f"https://api.github.com/repos/{username}/{repo_name}/commits"
        commits_response = requests.get(commits_url, timeout=10)

        if commits_response.status_code == 200:
            commits = commits_response.json()
            commit_count = len(commits)
        else:
            commit_count = 0

        results.append((repo_name, commit_count))

    return results


if __name__ == "__main__":
    user = "richkempinski"
    data = get_repo_commit_counts(user)
    for repo, count in data:
        print(f"Repo: {repo} Number of commits: {count}")
