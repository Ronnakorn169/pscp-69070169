"""docstring module"""
import math
def main():
    """main function"""
    size , amount = map(int,input().split(" "))
    n = 0
    row = 0
    while n < amount:
        row += 1
        n += row
    print(int(math.ceil(row/size)))
main()
