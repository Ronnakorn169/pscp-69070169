"""docstring module"""
def main():
    """main function"""
    l, n = map(int, input().split())
    bridges = [0] * l
    for _ in range(n):
        a, b = map(int, input().split())
        for i in range(a, b):
            bridges[i] += 1
    print(max(bridges))
main()
