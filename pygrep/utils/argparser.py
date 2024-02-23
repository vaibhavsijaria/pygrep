import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("pygrep",description="grep replica written in py")
    parser.add_argument("searchStr")
    parser.add_argument("path")
    parser.add_argument("-r","--recursive",action="store_true")
    parser.add_argument("-i","--ignore-case",action="store_true")
    parser.add_argument("-c","--count",action="store_true")

    return parser.parse_args()