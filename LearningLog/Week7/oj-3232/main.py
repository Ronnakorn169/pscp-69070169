"""jump step frog"""
def main():
    """main function"""
    step , goal = map(int,input().split(" "))
    total = 0
    countStep = 0
    while total < goal:
        total += step
        countStep += 1
        step -= 2
        if step <= 0 and total < goal:
            countStep = -1
            break
    print(countStep)
main()
