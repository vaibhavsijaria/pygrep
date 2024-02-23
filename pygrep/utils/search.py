import re

def str_search(content,search_obj,ignore_case = None) -> list:
    flags = re.IGNORECASE if ignore_case else 0
    matches = list(re.finditer(search_obj,content,flags))
    return matches