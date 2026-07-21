"""docstring module"""
def main():
    """main"""
    money = int(input())
    #/
    baht10 = money // 10
    money -= baht10*10
    #/
    baht5 = money // 5
    money -= baht5*5
    #/
    baht2 = money // 2
    money -= baht2*2
    #/
    baht1 = money // 1
    money -= baht10*1
    #/
    print(f"10 = {baht10}")
    print(f"5 = {baht5}")
    print(f"2 = {baht2}")
    print(f"1 = {baht1}")
main()
