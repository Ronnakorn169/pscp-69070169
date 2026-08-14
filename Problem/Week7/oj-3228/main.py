"""docstring module"""
def main():
    """main function"""
    money = input()
    year = int(input())
    if "." in money:
        money1,money2 = money.split(".", maxsplit=1)
        money2 = (money2 + "00")[:2]
    else:
        money1 = money
        money2 = "00"
    money = int(money1) * 100 + int(money2)
    for _ in range(year):
        money = money * 10381 // 10000
    print(f"{money // 100}.{money % 100:02d}")
main()
