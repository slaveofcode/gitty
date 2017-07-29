from dulwich.repo import Repo
from .config import Config


class Gitty:
  repository = None
  
  def __init__(self, repo_path):
    self.repository = Repo(repo_path)

  def config(self, config_param):
    return Config.get(self.repository, config_param)