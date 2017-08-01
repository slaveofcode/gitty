from os.path import dirname, basename
from dulwich.client import TCPGitClient

class Client:
    remote_url = None
    client = None

    def __init__(self, remote_address, remote_port):
        self.remote_url = remote_address

        path = dirname(remote_address)
        self.client = TCPGitClient(path.encode('ascii'), remote_port)

    def fetch(self, repo):
        repo_name = basename(self.remote_url)
        self.client.fetch(repo_name.encode(), repo)
