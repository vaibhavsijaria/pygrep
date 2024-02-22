from termcolor import colored

def printOutput(content,matches):
    for match in matches:
        start, end = match.span()
        print(start,end)
        content = content[:start] + colored(content[start:end], 'red') + content[end:]
    print(content)
