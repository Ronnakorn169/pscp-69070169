"""docstring module"""
import datetime
def main():
    """main function"""
    #/ first friend
    y1 = int(input())
    m1 = int(input())
    d1 = int(input())
    #/ second friend
    y2 = int(input())
    m2 = int(input())
    d2 = int(input())
    date1 = datetime.date(y1, m1, d1)
    date2 = datetime.date(y2, m2, d2)
    diff = (date1 - date2).days
    if abs(diff) <= 7:
        print(0)
    elif diff > 7:
        print(2)
    elif diff < -7:
        print(1)
main()
