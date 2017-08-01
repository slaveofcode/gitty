import os
import sys
from gitty import Gitty


if __name__ == "__main__":
    current_dir = os.path.dirname(os.path.realpath(__file__))
    git = Gitty(current_dir)
    print(current_dir)
    print(sys.argv)
