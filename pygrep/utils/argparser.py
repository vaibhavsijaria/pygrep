import argparse

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="pygrep",
        description="A Python implementation of the grep command. "
                    "Searches for a pattern in the specified files and prints matching lines.",
        usage="%(prog)s [options] pattern file..."
    )
    parser.add_argument(
        "searchStr",
        help="The pattern to search for. Can be a simple string or a regular expression."
    )
    parser.add_argument(
        "path",
        nargs="+",
        help="One or more files to search. If multiple files are specified, they should be separated by spaces."
    )
    parser.add_argument(
        "-r",
        "--recursive",
        action="store_true",
        help="If specified, search for the pattern recursively in directories."
    )
    parser.add_argument(
        "-i",
        "--ignore-case",
        action="store_true",
        help="If specified, ignore case distinctions in the pattern and the file."
    )
    parser.add_argument(
        "-c",
        "--count",
        action="store_true",
        help="If specified, instead of printing the matching lines, print a count of the number of lines that match the pattern."
    )

    return parser.parse_args()