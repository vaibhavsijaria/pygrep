from .utils.reader import read_file, file_handler
from .utils.search import str_search
from .utils.output import printOutput
from .utils.argparser import parse_args

import argparse

def main():
    args = parse_args()
    searchStr = args.searchStr
    path = args.path

    for file_path in file_handler(path,args.recursive):
        for line in read_file(file_path):
            matches = str_search(line,searchStr)
            printOutput(line,matches)


if __name__ == "__main__":
    main()