"""docstring module"""
def main():
    """main function"""
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    list_num = [num1,num2,num3]
    num_dupe = 0
    for i in list_num:
        dupe = list_num.count(i)
        if dupe > num_dupe:
            num_dupe = dupe
    match num_dupe:
        case 1:
            print("all different")
        case 2:
            print("neither")
        case 3:
            print("all the same")
main()
