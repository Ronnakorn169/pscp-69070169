"""docstring module"""
def main():
    """main function"""
    amountRound = int(input())
    fire = 0
    water = 0
    earth = 0
    for _ in range(amountRound):
        fire1, water1, earth1, fire2, water2, earth2 =\
        map(int,input().split(" "))
        fire += max(fire1,fire2)
        water += max(water1,water2)
        earth += max(earth1,earth2)
    total = fire+water+earth
    bonus = "YES" if fire > earth+water else "NO"
    print("Total:",total)
    print("Fire:",fire)
    print("Water:",water)
    print("Earth:",earth)
    print("Bonus:",bonus)
main()
