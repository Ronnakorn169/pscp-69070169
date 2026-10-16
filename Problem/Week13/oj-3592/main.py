"""docstring module"""
import math
def main():
    """main function"""
    size = int(input())
    align = input()
    text = input()
    if align == "left":
        print(text+" "*(size-len(text)))
    elif align == "right":
        print((" "*(size-len(text)) + text))
    elif align == "center":
        space = size-len(text)
        print(" " * math.ceil(space / 2) + text + " " * math.floor(space / 2))
main()
