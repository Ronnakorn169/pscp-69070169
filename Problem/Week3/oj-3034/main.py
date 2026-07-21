"""docstring module"""
def main():
    """main func"""
    pax,row = map(int,input().split(" "))
    pax_order = []
    for _ in range(pax):
        order_row = int(input())
        pax_order.append(order_row)
    pax_order.sort()
    row_order = []
    for i in range(row):
        row_order.append(i+1)
    while True:
        isHasRow = True
        for i in row_order:
            if not i in pax_order:
                isHasRow = False
        if isHasRow:
            for i in row_order:
                pax_order.remove(i)
        else:
            break
    print(len(pax_order))
main()
