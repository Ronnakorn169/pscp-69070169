"""docstring module"""
def main():
    """main function"""
    array_num = []
    last_input = 1
    while last_input:
        if len(array_num) != 3:
            array_num.append(int(input()))
            print(f"Input number {len(array_num)} stored.")
            continue
        last_input = int(input())
        if last_input == 2:
            new_arr = sorted(array_num,reverse=True)
            print("Descending order:"," ".join(map(str,new_arr)))
        elif last_input == 1:
            print("Original order:"," ".join(map(str,array_num)))
        elif last_input == 3:
            new_arr = sorted(array_num,reverse=False)
            print("Ascending order:"," ".join(map(str,new_arr)))
main()
