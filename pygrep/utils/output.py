from termcolor import colored

def printOutput(content,matches,file_name = None):
    if not matches and file_name:
        return
    
    if file_name:
        file_name = colored(file_name,"magenta")+colored(":","cyan")
        print(file_name,end="")
    
    for match in reversed(matches):
        start, end = match.span()
        content = content[:start] + colored(content[start:end], 'red') + content[end:]
    print(content)
