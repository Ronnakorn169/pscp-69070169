"""docstring module"""
import math
def main():
    """main function"""
    membership = input().strip()
    item_count = int(input())
    price_result = 0
    for _ in range(item_count):
        price_result += float(input())
    discount_multiply = .95 if membership == "Y" else .97 \
    if membership != "Y" and price_result >= 500 else 1
    price_result *= discount_multiply
    print(f"{math.ceil(1.233567*100)/100:.2f}")
main()
