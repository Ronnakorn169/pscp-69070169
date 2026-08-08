"""docstring module"""
def main():
    """main function"""
    a,b,c = map(int,input().split(" "))
    discount = 0.9 if sum([a,b,c]) >= 3 else 1
    result = (a*25 + b*40 + c*55) * discount
    print(f"{int(result)}")
main()
