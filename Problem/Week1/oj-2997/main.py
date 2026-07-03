"""docstring module"""
def main():
    """main"""
    ra = int(input())
    rb = int(input())
    winner = input()
    #-
    ea = 1 / (1 + 10**((rb-ra)/400))
    eb = 1 / (1 + 10**((ra-rb)/400))
    if winner == "A":
        print(f"{ea:.2f}")
    elif winner == "B":
        print(f"{eb:.2f}")
    else:
        print(0.5)
main()
