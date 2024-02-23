from .utils.reader import read_file, file_handler
from .utils.search import str_search
from .utils.output import printOutput
from .utils.argparser import parse_args

import argparse

def main():
    args = parse_args()
    searchStr = args.searchStr
    paths = args.path
    c = 0
    for path in paths:
        for file_path in file_handler(path,args.recursive):
            for line in read_file(file_path):
                file_path = file_path if args.recursive or len(paths) > 1 else None
                matches = str_search(line,searchStr,args.ignore_case)
                if args.count:
                    c += 1 if len(matches) else 0
                else:
                    printOutput(line,matches,file_path)

    if args.count:
        print(c)

if __name__ == "__main__":
    main()