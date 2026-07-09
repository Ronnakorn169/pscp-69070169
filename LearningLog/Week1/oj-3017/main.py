"""module"""
def main():
    """main"""
    price = int(input())
    service_price = price * 10 / 100
    if service_price < 50:
        service_price = 50
    elif service_price > 1000:
        service_price = 1000
    price = (price+service_price) * 107 / 100
    print(f"{price:.2f}")
main()
