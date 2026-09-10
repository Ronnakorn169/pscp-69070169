"""pizza"""
def main():
    """main function"""
    people = int(input())
    want_per_people = int(input())
    pizza = int(input())
    #/
    all_need_pizza = people*want_per_people
    pizza_order = all_need_pizza//pizza
    if all_need_pizza%pizza:
        pizza_order += 1
    print(all_need_pizza)
    print(pizza_order)
    print(abs(all_need_pizza-(pizza_order*pizza)))
main()
