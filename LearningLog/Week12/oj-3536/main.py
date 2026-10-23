"""docstring module"""
def main():
    """main function"""
    num = int(input())
    if num < 2:
        print("NO")
        return
    if num == 2:
        print("YES")
        return
    if not num % 2:
        print("NO")
        return

    limit = int(num ** 0.5)
    for div in range(3, limit + 1, 2):
        if not num % div:
            print("NO")
            return

    print("YES")

main()
