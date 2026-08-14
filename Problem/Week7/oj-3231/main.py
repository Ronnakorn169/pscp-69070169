"""docstring module"""
def main():
    """main function"""
    p1 = int(input())
    p2 = int(input())
    if not 1 <= p1 <= 6 or not 1 <= p2 <= 6:
        print("Invalid")
        return
    if p1 != p2:
        print("Wrong!")
    else:
        print("Correct!")
main()
