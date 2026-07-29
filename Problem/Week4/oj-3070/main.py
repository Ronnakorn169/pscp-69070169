"""docstring module"""
def main():
    """main function"""
    even = 0
    odd = 0
    for _ in range(3):
        num = int(input())
        even += 1 if not (num % 2) else 0
        odd += 1 if (num % 2) else 0
    print(even)
    print(odd)
main()
