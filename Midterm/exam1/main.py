"""stats"""
def main():
    """main function"""
    n = int(input())
    sum_all = 0
    min_num = 0
    max_num = 0
    for i in range(n):
        num = int(input())
        if not i:
            min_num = num
            max_num = num
        else:
            if num < min_num:
                min_num = num
            if num > max_num:
                max_num = num
        sum_all += num
    avg = sum_all / n if n > 0 else 0
    print(f"MIN: {min_num:.3f}")
    print(f"MAX: {max_num:.3f}")
    print(f"AVG: {avg:.3f}")
main()
