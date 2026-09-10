"""docstring"""
def main():
    """main"""
    x_str, k = input().split()
    x = int(x_str)
    mid = x // 2
    for i in range(x):
        dist = abs(i - mid)
        row = []
        for j in range(x):
            if j in (i ,x - 1 - i):
                row.append('#' if k == '#' else chr(ord(k) + dist))
            else:
                row.append('-')
        print(''.join(row))
main()
