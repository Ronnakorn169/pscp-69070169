"""docstring module"""
def main():
    """main func"""
    original_price = int(input())
    cap_for_promotion = int(input())
    promotion_price = int(input())
    objective = int(input())
    if not objective:
        print(0)
        return
    if not cap_for_promotion:
        print(original_price * objective)
        return
    promo_items = (objective - 1) // cap_for_promotion
    normal_items = objective - promo_items
    #/
    total_price = (normal_items * original_price) + (promo_items * promotion_price)
    print(total_price)
main()
