"""docstring module"""
def main():
    """main function"""
    num = int(input())
    if num == 1:
        print(1)
        return

    ans = num
    length = len(str(num))
    for i in range(1, length):
        ans += 9 * (10 ** (i - 1)) * i

    ans += (num - (10 ** (length - 1)) + 1) * length
    print(ans)

main()
