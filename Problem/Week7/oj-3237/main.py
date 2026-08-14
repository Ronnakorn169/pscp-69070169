"""docstring module"""
def main():
    """main function"""
    n = int(input())
    for i in range(n):
        for j in range(i+1):
            if not j:
                print(0,end="")
            else:
                if j != i:
                    if i != n-1:
                        print(1,end="")
                    else:
                        print(0,end="")
                else:
                    print(0,end="")
        print("")
main()
