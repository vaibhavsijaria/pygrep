from pathlib import Path
from typing import Union, Generator

def read_file(file_path: Union[str, Path]) -> Generator[str, None, None]:
    try:
        with open(Path(file_path), 'r') as file:
            for line in file:
                yield line.strip()
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")