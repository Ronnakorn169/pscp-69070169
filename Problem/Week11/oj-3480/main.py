"""docstring module"""
def main():
    """main function"""
    n = int(input())
    h = [0] + list(map(int, input().split())) + [0]
    count = 0
    for i in range(1, n + 1):
        if h[i] > h[i - 1] and h[i] > h[i + 1]:
            count += 1
    print(count)
main()
