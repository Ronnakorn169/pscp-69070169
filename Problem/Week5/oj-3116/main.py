"""docstring module"""
def main():
    """main function"""
    school_name = input()
    key_dict = {
            1 : 0,
            2 : 1,
            3 : 2,
            4 : 3,
            5 : 4,
            6 : 5,
            7 : 6,
            8 : 7,
            9 : 8,
            10 : 9,
        }
    #/ First Step:
    f_name = school_name[0].upper()
    l_name = school_name[-1].upper()
    for i in range(1,11):
        if i%2:
            key_dict[i] += ord(f_name)
        else:
            key_dict[i] -= ord(l_name)
    #/ Second Step:
    amount_word = len(school_name)
    for i in range(1,11):
        key_dict[i] = abs(key_dict[i]) % amount_word
        if key_dict[i] > 9:
            key_dict[i] %= 10
    password = ""
    for i in range(3, 9):
        password += str(key_dict[i]) + " "
    print(password)
main()
