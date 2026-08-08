""""docstring module"""
def main():
    """main function"""
    n = int(input())
    for i in range(1,n+1):
        if i%5:
            print("*",end="")
        else:
            print("X",end="")
main()
