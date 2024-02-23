from pathlib import Path
from typing import Union, Generator
import os
import glob

def read_file(file_path: Union[str, Path]) -> Generator[str, None, None]:
    try:
        with open(Path(file_path), 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)} while reading {file_path}")

# def r_file_iter(dir):
#     for root, dirs, files in os.walk(dir):
#         for file in files:
#             yield os.path.join(root, file)

# def dir_handler(pattern, include_dir):
#     for path in glob.glob(pattern):
#         if os.path.isdir(path) and not include_dir:
#             continue
#         yield path

def file_handler(pattern, is_recursive):
    for path in glob.glob(pattern):
        if os.path.isdir(path):
            if is_recursive:
                for root, _, files in os.walk(path):
                    for file in files:
                        yield os.path.join(root, file)
            else:
                continue
        else:
            yield path