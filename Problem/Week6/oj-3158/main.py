""""docstring module"""
def main():
    """main function"""
    n = int(input())
    total = 0
    for i in range(1,n+1):
        total += i ** 2
    print(total)
main()
