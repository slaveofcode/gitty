from dulwich.repo import Repo

def init(repo_path):
    return Repo.init(repo_path, mkdir=True)

def open(repo_path):
    return Repo(repo_path)