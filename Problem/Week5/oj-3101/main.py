"""docstring module"""
def main():
    """main function"""
    temp = int(input())
    type_temp = input().lower()
    if type_temp == "c":
        temp = (temp * 9/5) + 32
    if 32<temp<212:
        print("liquid")
    elif temp >= 212:
        print("gas")
    else:
        print("solid")
main()
