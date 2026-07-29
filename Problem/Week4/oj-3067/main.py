"""docstring module"""
def main():
    """main function"""
    num1 = float(input())
    num2 = float(input())
    num3 = float(input())
    list_num = [num1,num2,num3]
    state = 0
    for i in range(1,len(list_num)):
        if list_num[i] > list_num[i-1] and state != -1:
            state = 1
        elif list_num[i] < list_num[i-1] and state != 1:
            state = -1
        else:
            state = 999
            print("neither")
            break
    if state == 1:
        print("increasing")
    elif state == -1:
        print("decreasing")
main()
