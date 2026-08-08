"""docstring module"""
def main():
    """main function"""
    age , day = map(str,input().split(" "))
    age = int(age)
    price = 0
    price = 0 if age < 5 else 100 if 5 <= age <= 18 else 150
    if day == "Wed":
        price /= 2
    print(f"{price:.0f}")
main()
