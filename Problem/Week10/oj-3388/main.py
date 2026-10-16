"""docstring module"""
def main():
    """main function"""
    num = input()
    is_over = False
    while not is_over:
        num = num.replace("113","")
        if num.find("113") == -1:
            is_over = True
    print(num)
main()
