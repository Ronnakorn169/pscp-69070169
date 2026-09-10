"""Triangle"""
def main():
    """main function"""
    a = int(input())
    b = int(input())
    c = int(input())
    if not a+b > c or not a+c > b or not c+b > a:
        print("NOT A TRIANGLE")
        return
    if a == b and b == c and c == a:
        print("EQUILATERAL")
    elif (a**2) + (b**2) == c**2:
        print("RIGHT TRIANGLE")
    elif (a == b and b != c and a != c) or (b == c and c != a and b != a) \
        or (c == a and c != b and a != b):
        print("ISOSCELES")
    elif a != b and b != c and c != a:
        print("SCALENE")
main()
