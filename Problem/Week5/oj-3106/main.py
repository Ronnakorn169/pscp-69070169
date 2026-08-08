"""docstring module"""
def main():
    """main function"""
    money = int(input())
    if money%100:
        print("ERROR")
        return
    money_dict = {1000:0,
                  500:0,
                  100:0}
    money_dict[1000] = money//1000
    money -= (money//1000)*1000
    money_dict[500] = money//500
    money -= (money//500)*500
    money_dict[100] = money//100
    for i in money_dict.items():
        if i[1]:
            print(f"{i[0]} = {i[1]}")
main()
