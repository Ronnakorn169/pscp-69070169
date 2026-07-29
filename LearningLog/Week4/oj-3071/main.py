"""docstring module"""
def main():
    """main function"""
    start = int(input())
    end = int(input())
    divide_num = int(input())
    goal = int(input())
    count = 0
    for i in range(start,end+1):
        count += 1 if i%divide_num == goal else 0
    print(count)
main()
