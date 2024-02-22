import re

def str_search(content,search_obj) -> list:
    matches = list(re.finditer(search_obj,content))
    return reversed(matches)