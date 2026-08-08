"""docstring module"""
def main():
    """main function"""
    n = int(input())
    total = 0
    highest_sell = 0
    lowest_sell = 0
    for i in range(n):
        sells = int(input())
        #/ default value
        if not i:
            highest_sell = sells
            lowest_sell = sells
        #/
        highest_sell = sells if sells > highest_sell else highest_sell
        lowest_sell = sells if sells < lowest_sell else lowest_sell
        total += sells
    average = total / n
    print(total)
    print(highest_sell)
    print(lowest_sell)
    print(f"{average:.1f}")
main()
