""""docstring module"""
def main():
    """main function"""
    num = input()[::-1]
    new_num = ""
    for i in range(1,len(num)+1):
        is_col = False
        if not i%3 and i != len(num):
            is_col = True
        new_num += num[i-1]+"," if is_col else num[i-1]
    new_num = new_num[::-1]
    print(new_num)
main()
