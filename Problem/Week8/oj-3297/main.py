"""movie ticket"""
def main():
    """main function"""
    tickets_left = int(input())
    while tickets_left > 0:
        try:
            age,ticket_want = map(int,input().split(" "))
            if age <= 14:
                print(-1)
                continue
            if ticket_want > tickets_left:
                print(-2)
                continue
            price = 150*ticket_want
            if 15 <= age <= 22:
                price *= 0.8
            elif age >= 60:
                price *= 0.5
            tickets_left -= ticket_want
            print(int(price),tickets_left)
        except EOFError:
            break
main()
