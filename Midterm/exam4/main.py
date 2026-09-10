"""Thai Plus"""
def money_cal(stats,family):
    """calculate money"""
    money = 0
    if stats == "GOLD":
        money = 3000
    elif stats == "SILVER":
        money = 1500
    if family >= 3:
        money += 500
    return money
def main():
    """main function"""
    name = input()
    age = int(input())
    salary = int(input())
    card = input()
    family = int(input())
    #/
    Stats = ""
    if age < 18:
        print(name,"NOT ELIGIBLE")
        return
    if card == "Y":
        Stats = "GOLD"
    elif salary <= 15000:
        Stats = "GOLD"
    elif salary <= 30000:
        Stats = "SILVER"
    else:
        print(name,"NOT ELIGIBLE")
        return
    if not Stats:
        print(name,"NOT ELIGIBLE")
        return
    money = money_cal(Stats,family)
    print(name,Stats,money)
main()
