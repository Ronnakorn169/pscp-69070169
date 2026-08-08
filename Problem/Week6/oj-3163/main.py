""""docstring module"""
def main():
    """main function"""
    n = int(input())
    total = 0
    even = 0
    odd = 0
    for _ in range(n):
        stock = int(input())
        total += stock
        even += 1 if not stock%2 else 0
        odd += 1 if stock%2 else 0
    print("SUM",total)
    print("EVEN",even)
    print("ODD",odd)
main()
