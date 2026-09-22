"""docstring module"""
def main():
    """main function"""
    n = int(input())
    dishes = []
    for _ in range(n):
        dishes.append(int(input()))
    count = 0
    dishes = sorted(dishes)
    while dishes:
        p_num = 0
        temp_dish = dishes.copy()
        for i in temp_dish:
            if not p_num:
                p_num = i
                dishes.remove(i)
                continue
            if p_num < i:
                p_num = i
                dishes.remove(i)
        count += 1
    print(count)
main()
