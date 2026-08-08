"""docstring module"""
def main():
    """main function"""
    n = int(input())
    count = 0
    for _ in range(n):
        command = input()
        count += 10 if command == "+" else -5
    print(count)
main()
