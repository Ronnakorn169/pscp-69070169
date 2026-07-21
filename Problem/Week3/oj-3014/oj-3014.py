"""docstring main"""
def main():
    """main"""
    price = int(input())
    to_promotion = int(input())
    bonus = int(input())
    cur_money = int(input())
    #/
    can_buy = cur_money // price
    result_bottle = can_buy
    bonus_bottle = 0
    if can_buy >= to_promotion and to_promotion:
        exchanges = (can_buy - bonus) // (to_promotion - bonus)
        bonus_bottle = exchanges * bonus
        result_bottle += bonus_bottle
    print(result_bottle)
main()
