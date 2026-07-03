"""docstring module"""
import math
def main():
    """main"""
    a = float(input())
    b = float(input())
    c = float(input())
    s = (a+b+c)/2
    Area = math.sqrt((s*(s-a)*(s-b)*(s-c)))
    print(f"{Area:.3f}")
main()
