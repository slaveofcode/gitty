# Gitty
A simple git operations for human based on dulwich project and Python3, most of these operations are base on very basic command on git. 

    command
    sc=ssss

## List of Supported Commands
- [`git config`](https://github.com/slaveofcode/gitty#git-config)
- `git clone`
- `git fetch`
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

#### git config

get config value from the repository config file `eg: .git/config`, so if you get something like global config or some value that not exist on that file, it would return `None` value.

    from gitty import Gitty

    git = Gitty('.') // set repo on current directory 

    // git config user.name
    git.config('user.name')  // 'Aditya Kresna Permana'

    // git config user.email
    git.config('user.email')  // 'zeandcode@gmail.com'

    // git config remote.origin.url
    git.config('remote.origin.url)  // https://github.com/slaveofcode/gitty.git




# Install
    pip install gitty

# Documentation
...coming soon
