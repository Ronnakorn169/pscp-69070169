"""docstring module"""
#gonna test brute force
def check_num(num_hint,num,operater):
    """compare function"""
    match operater:
        case "==":
            return num == num_hint
        case ">=":
            return num >= num_hint
        case ">":
            return num > num_hint
        case "<=":
            return num <= num_hint
        case "<":
            return num < num_hint
        case "!=":
            return num != num_hint
def main():
    """main function"""
    onePlace = input()
    tenPlace = input()
    hundredPlace = input()
    list_hint = [hundredPlace,tenPlace,onePlace]
    for i in range(0,1000):
        check = True
        for index,j in enumerate(list_hint):
            operator = j.split(" ")[0]
            numhint = int(j.split(" ")[1])
            check = check_num(num_hint=numhint,
                            operater=operator,
                            num=int(f"{i:03d}"[index]))
            if not check:
                break
        if check:
            print(f"{i:03d}")
main()
