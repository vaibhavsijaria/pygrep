from .utils.reader import read_file
from .utils.search import str_search
from .utils.output import printOutput

import argparse

def main():
    parser = argparse.ArgumentParser("pygrep",description="grep replica written in py")
    parser.add_argument("searchStr")
    parser.add_argument("path")
    args = parser.parse_args()
    searchStr = args.searchStr
    file_path = args.path
    content = read_file(file_path)
    matches = str_search(content,searchStr)
    printOutput(content,matches)


if __name__ == "__main__":
    main()