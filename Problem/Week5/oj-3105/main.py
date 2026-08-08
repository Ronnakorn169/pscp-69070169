"""docstring module"""
def main():
    """main function"""
    distance = int(input())
    money = 0
    if distance > 10:
        money += 45 + ((distance - 10) * 8)+35
    elif distance >= 1:
        money += (max(0,(distance - 1)) * 5)+35
    print(money)
main()
