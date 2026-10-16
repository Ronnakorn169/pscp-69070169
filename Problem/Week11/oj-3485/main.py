"""docstring module"""
def main():
    """main function"""
    _ = int(input())
    items = list(map(int, input().split()))
    counts = {}
    for x in items:
        counts[x] = counts.get(x, 0) + 1
    rare = sorted(x for x, count in counts.items() if count == 1)
    print(*rare)
main()
