"""docstring module"""
def main():
    """main function"""
    score1 = int(input())
    score2 = int(input())
    score3 = int(input())
    if score1 < 5 or score2 < 20 or score3 < 25:
        print("fail")
    else:
        print("pass")
main()
