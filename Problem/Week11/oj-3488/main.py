"""docstring module"""
def main():
    """main function"""
    n = int(input())
    lit = [0] * 360
    for _ in range(n):
        a, b = map(int, input().split())
        if a < b:
            for i in range(a, b):
                lit[i] = 1
        else:
            for i in range(a, 360):
                lit[i] = 1
            for i in range(0, b):
                lit[i] = 1
    if sum(lit) == 360:
        print(360)
    else:
        max_len = 0
        cur_len = 0
        for x in lit + lit:
            if x == 1:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 0
        print(max_len)
main()
