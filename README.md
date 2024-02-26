# PyGrep: Python Grep Implementation

PyGrep is a Python-based implementation of the Unix `grep` command. It provides a simple and intuitive way to search for patterns within specified files, displaying any matching lines.

## 🚀 Features

- **Pattern Search:** Search for a specific pattern within one or more files.
- **Recursive Search:** Perform a recursive search within directories.
- **Case-Insensitive Search:** Perform a search without considering case distinctions.
- **Count Matches:** Count the number of matching lines without printing them.

## 📖 Usage

Use the following command to run PyGrep:

```sh
python3 -m pygrep [options] pattern file...
```

### Options
- `pattern`: The pattern to search for. Can be a simple string or a regular expression.
- `file...`: One or more files to search. If multiple files are specified, they should be separated by spaces.
- `-r`,` --recursive`: If specified, search for the pattern recursively in directories.
- `-i`,` --ignore-case`: If specified, ignore case distinctions in the pattern and the file.
- `-c`,` --count`: If specified, instead of printing the matching lines, print a count of the number of lines that match the pattern.

## 💾 Installation
1. Clone the repository:
```sh
git clone https://github.com/yourusername/pygrep.git
```
2. Navigate to the project directory:
```sh
cd pygrep
```
3. Install the required packages:
```sh
pip install -r requirements.txt
```

