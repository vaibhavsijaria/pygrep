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
            file_path = file_path if args.recursive else None
            matches = str_search(line,searchStr,args.ignore_case)
            printOutput(line,matches,file_path)


if __name__ == "__main__":
    main()