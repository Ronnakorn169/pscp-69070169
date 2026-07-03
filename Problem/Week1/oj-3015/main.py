"""module"""
def main():
    """main"""
    promotion_come = int(input())
    promotion_pay = int(input())
    real_price = int(input())
    actual_come = int(input())
    #
    promotion_free = promotion_come - promotion_pay
    actual_free = (actual_come // promotion_come) * promotion_free
    price_calculate = (actual_come - actual_free) * real_price
    print(price_calculate)
main()
