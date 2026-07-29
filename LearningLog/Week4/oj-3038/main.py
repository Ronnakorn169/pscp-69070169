"""docstring module"""
def main():
    """main function"""
    #/Rock size
    small = int(input())
    big = int(input())
    goal = int(input())
    #/
    big_need = goal // (5)
    small_need = goal-(min(big,big_need)*5)
    if small_need > small:
        print(-1)
    else:
        print(small_need)
main()
