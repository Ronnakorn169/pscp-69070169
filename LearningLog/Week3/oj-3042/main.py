"""docstring module"""
def main():
    """main"""
    num = int(input())
    num = num - (num%10)
    for _ in range(int(num/10)+1):
        if num:
            print(num,end=" ")
        else:
            print(num)
        num -= 10
main()
