# Gitty
A simple git operations for human based on dulwich project and Python3, most of these operations are base on very basic command on git. 

## List of Supported Commands
- [`git config`](https://github.com/slaveofcode/gitty#git-config)
- [`git clone`](https://github.com/slaveofcode/gitty#git-clone)
- [`git fetch`](https://github.com/slaveofcode/gitty#git-fetch)
- `git init`
- `git remote`
- `git add`
- `git rm`
- `git status`
- `git commit`
- `git diff`
- `git log`
- `git blame`
- `git pull`
- `git push`
- `git branch`
- `git checkout`
- `git tag`
- `git reset`
- `git revert`
- `git clean`
- `git merge`
- `git rebase`
- `git stash`
- `git archive`

#### Git Config

get config value from the repository config file `eg: .git/config`, so if you get something like global config or some value that not exist on that file, it would return `None` value.

    from gitty import Gitty

    git = Gitty('.') # set repo path, default is on current directory 

    # git config user.name
    git.config('user.name')  # 'Aditya Kresna Permana'

    # git config user.email
    git.config('user.email') # 'zeandcode@gmail.com'

    # git config remote.origin.url
    git.config('remote.origin.url)  # https://github.com/slaveofcode/gitty.git


#### Git Clone

clone a repository.

    from gitty import Gitty
    Gitty.clone('https://github.com/slaveofcode/gitty.git', 'path-clone-folder')

#### Git Fetch

fetch from remote server

    from gitty import Gitty
    git = Gitty('.')  # set repo path, default is on current directory 
    git.fetch()


# Install
    pip install gitty
