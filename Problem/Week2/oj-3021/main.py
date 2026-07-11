"""docstring module"""
import math
#/Good Referance:http://mathinschool.com/page/473.html
def main():
    """main"""
    #/ Circle1
    x1 = int(input())
    y1 = int(input())
    r1 = int(input())
    #/ Circle2
    x2 = int(input())
    y2 = int(input())
    r2 = int(input())
    #/
    d = math.sqrt( ((x1-x2)**2)+((y1-y2)**2) )
    if d < r1+r2:
        print("overlapping")
    else:
        print("no overlapping")
main()
