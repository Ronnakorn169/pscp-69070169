"""docstring module"""
def main():
    """main function"""
    text = input()
    shift = int(input())
    for ch in text:
        print(chr((ord(ch) + shift - 97) % 26 + 97),end="")
main()
