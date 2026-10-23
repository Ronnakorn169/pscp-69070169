"""docstring module"""
def main():
    """main function"""
    num = int(input())
    is_sqfree = [1] * (num + 1)
    is_sqfree[0] = 0
    limit = int(num ** 0.5)
    for base in range(2, limit + 1):
        square = base * base
        for multiple in range(square, num + 1, square):
            is_sqfree[multiple] = 0
    print(sum(is_sqfree))
main()
