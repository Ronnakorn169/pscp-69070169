"""docstring module"""
def main():
    """main function"""
    n = int(input())
    normal_work = 0
    high_work = 0
    for _ in range(n):
        work = int(input())
        normal_work += 1 if work <= 18 else 0
        high_work += 1 if work > 18 else 0
    high_work_left = max(0,high_work-normal_work)
    total = normal_work+high_work+high_work_left
    total -= 1 if high_work > normal_work else 0
    print(total)
main()
