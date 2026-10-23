"""docstring module"""
def main():
    """main function"""
    stock = {}
    while True:
        line = input().strip()
        if line == "END":
            break
        parts = line.split()
        cmd = parts[0]

        if cmd == "ADD":
            name = parts[1]
            amount = int(parts[2])
            stock[name] = stock.get(name, 0) + amount
        elif cmd == "REMOVE":
            name = parts[1]
            amount = int(parts[2])
            current = stock.get(name, 0)
            if current >= amount:
                stock[name] = current - amount
            else:
                stock[name] = 0
                print(f"Not enough stock for {name}")
        elif cmd in ("CHECK", "CHECKREPORT"):
            low_items = [k for k, v in sorted(stock.items()) if v < 5]
            if low_items:
                for item in low_items:
                    print(item)
            else:
                print("All stocks are sufficient")
        elif cmd == "REPORT":
            for name in sorted(stock):
                print(f"{name}: {stock[name]}")

main()
