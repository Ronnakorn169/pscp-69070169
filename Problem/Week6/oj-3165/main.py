""""docstring module"""
def main():
    """main function"""
    n = input()
    x = 0
    y = 0
    for i in n:
        x += 1 if i == "E" else -1 if i == "W" else 0
        y += 1 if i == "N" else -1 if i == "S" else 0
    print(f"{x} {y} {abs(x)+abs(y)}")
main()
