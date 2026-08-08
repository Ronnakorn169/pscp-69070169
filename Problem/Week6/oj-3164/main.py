"""docstring module"""
def main():
    """main function"""
    n = int(input())
    numbers = []
    for _ in range(n):
        n1 = int(input())
        n2 = int(input())
        numbers.append(max(n1,n2))
    result = sum(numbers)
    member_count = len(numbers)
    if member_count != 1:
        for i in range(member_count):
            if i != member_count-1:
                print(numbers[i],"+",end=" ")
            else:
                print(numbers[i],end=" ")
        print("=",result)
    else:
        print(result)
main()
