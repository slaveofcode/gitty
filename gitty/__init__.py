import os
import sys
from dulwich.repo import Repo
from dulwich import porcelain
from .config import Config
from .client import Client


class Gitty:
    repository = None
    client = None
  
    def __init__(self, repo_path='.'):
        self.repository = Repo(repo_path)
        self.client = self._initialize_client()
       
    def _initialize_client(self):
        remote_url = self.config('remote.origin.url')
        if remote_url:
            if remote_url.startswith('https://'):
                remote_port = 443
            elif remote_url.startswith('http://'):
                remote_port = 80
            elif remote_url.startswith('git://'):
                remote_port = 9418
            else:
                raise Exception('Unrecognize remote repository url for {}'.format(remote_url))

        print("{} {}".format(remote_url, remote_port))
        return Client(remote_url, remote_port)


    def config(self, config_param):
        return Config.get(self.repository, config_param)

    @staticmethod
    def clone(repo_link, local_folder='.'):
        porcelain.clone(repo_link, local_folder)

    def fetch(self):
        self.client.fetch(self.repository)

