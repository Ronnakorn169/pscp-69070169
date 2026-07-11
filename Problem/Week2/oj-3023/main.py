"""docstring module"""
def main():
    """main"""
    n = int(input())
    #/
    current_num = 0
    press_button_count = 0
    if n > 1:
        for _ in range(n):
            current_num += 1
            press_button_count += len(str(current_num))
            press_button_count += 1
        print(press_button_count)
    else:
        print(1)
main()
