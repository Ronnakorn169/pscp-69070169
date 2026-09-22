"""docstring module"""
def main():
    """main function"""
    temp = list(map(int,input().split(" ")))
    nums = []
    for v in temp:
        if not v % 5 or not v % 3:
            nums.append(v)
    nums = nums[::-1]
    if nums:
        for i in nums:
            print(i)
    else:
        print("Nope")
main()
