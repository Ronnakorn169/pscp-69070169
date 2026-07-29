"""docstring module"""
def main():
    """main function"""
    year = int(input())
    if not year%400:
        print("yes")
        return
    if year <= 1582 and not year%4:
        print("yes")
        return
    if year <= 1582 and year%4:
        print("no")
        return
    if (not year%4 and year%100):
        print("yes")
    else:
        print("no")
main()
