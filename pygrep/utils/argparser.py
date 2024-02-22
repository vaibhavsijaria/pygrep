import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser("pygrep",description="grep replica written in py")
    parser.add_argument("searchStr")
    parser.add_argument("path")

    return parser.parse_args()