"""docstring module"""
def main():
    """main function"""
    n, l = map(int, input().split())
    people = list(map(int, input().split()))
    chair_pos = list(map(int, input().split()))
    current_max = 0
    customer_idx = 0
    for i in range(n):
        if customer_idx < l and i + 1 == chair_pos[customer_idx]:
            people_height = people[i]
            if current_max >= people_height:
                print(current_max - people_height + 1)
            else:
                print(0)
            customer_idx += 1
        if people[i] > current_max:
            current_max = people[i]
main()
