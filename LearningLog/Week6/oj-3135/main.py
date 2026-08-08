"""docstring module"""
def main():
    """main function"""
    people , step , thief = map(int,input().split(" "))
    goal = [1,thief]
    if thief == 1:
        print(1)
        return
    current_gift = 0
    count = 0
    while True:
        if not current_gift:
            current_gift = 1
        current_gift += step
        while current_gift > people:
            current_gift -= people
        count += 1
        if current_gift in goal:
            count += 1 if current_gift == thief else 0
            break
    print(count)
main()
