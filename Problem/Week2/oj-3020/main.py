"""docstring module"""
def main():
    """main function"""
    original_price = int(input())
    cap_for_promotion = int(input())
    promotion_price = int(input())
    objective = int(input())
    #/
    if not cap_for_promotion:
        print(original_price*objective)
        return
    if not objective:
        print(0)
        return
    loop_promo = objective//cap_for_promotion
    price_result = original_price*(loop_promo)*(cap_for_promotion-1)
    price_result += promotion_price*loop_promo
    price_result += original_price
    if objective%cap_for_promotion:
        price_result += ((objective-1)%cap_for_promotion)*original_price
    else:
        price_result -= promotion_price
    print(price_result)
main()
