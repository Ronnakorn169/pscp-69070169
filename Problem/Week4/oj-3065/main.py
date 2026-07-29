"""docstring module"""
def main():
    """main function"""
    num = int(input())
    if num < 0:
        print("Error : Please input positive number")
        return
    if num > 9 or not num:
        print("Error : Out of range")
        return
    roman_num = {1:"I",
                 2:"II",
                 3:"III",
                 4:"IV",
                 5:"V",
                 6:"VI",
                 7:"VII",
                 8:"VIII",
                 9:"IX",
                }
    print(roman_num[num])
main()
