"""docstring module"""
def main():
    """main func"""
    a = int(input())
    order = []
    for _ in range(a):
        order.append(int(input()))
    order.sort()
    print(order[0])
main()
