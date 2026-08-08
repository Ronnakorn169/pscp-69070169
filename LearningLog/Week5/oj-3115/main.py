"""docstring module"""
def main():
    """main function"""
    shop_count = int(input().split(" ")[0])
    shops_schedule = []
    for _ in range(shop_count):
        start,end = map(int,input().split(" "))
        shops_schedule.append((start,end))
    checks_schedule = map(int,input().split(" "))
    result = []
    for i in checks_schedule:
        count = 0
        for j in shops_schedule:
            if j[0] <= i < j[1]:
                count += 1
        result.append(count)
    for i in result:
        print(i,end=" ")
main()
