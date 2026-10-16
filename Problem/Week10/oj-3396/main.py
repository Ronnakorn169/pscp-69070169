"""docstring module"""
def main():
    """main function"""
    n_k = input().split()
    n = int(n_k[0])
    k = int(n_k[1])
    s = [int(input()) for _ in range(n)]
    s_min = min(s)
    limit = k * s_min
    safe = 0
    if k == 1:
        print(n)
    else:
        for t in s:
            if (k - 1) * t < limit:
                safe += 1
        print(safe)
main()
