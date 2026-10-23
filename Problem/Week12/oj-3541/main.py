"""docstring module"""
def main():
    """main function"""
    price_a = int(input())
    cap_b = int(input())
    price_c = int(input())
    want_d = int(input())

    if not want_d:
        print(0)
    elif not cap_b:
        print(want_d * price_a)
    else:
        promo_count = (want_d - 1) // cap_b
        normal_count = want_d - promo_count
        total_cost = (normal_count * price_a) + (promo_count * price_c)
        print(total_cost)

main()
