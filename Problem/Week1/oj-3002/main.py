"""docstring module"""
def main():
    """main"""
    name = input()
    surname = input()
    age = input()
    password_generate = ""
    if len(name) >= 5 and len(surname) >= 5:
        pass1 = name[:2]
        pass2 = surname[len(surname)-1]
        pass3 = age[len(age)-1]
        password_generate = pass1+pass2+pass3
    else:
        pass1 = name[0]
        pass2 = surname[len(surname)-1]
        pass3 = age
        password_generate = pass1+pass3+pass2
    print(password_generate)
main()
