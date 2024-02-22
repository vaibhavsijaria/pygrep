from pathlib import Path
from typing import Union

def read_file(file_path: Union[str, Path]) -> str:
    try:
        with open(Path(file_path), 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File {file_path} not found.")
        return None
    except Exception as e:
        print(f"An unexpected error occurred: {str(e)}")
        return None