"""docstring module"""
def main():
    """main function"""
    n = int(input())
    count = 0
    most_weight = 0
    most_name = ""
    for _ in range(n):
        bunny_name , weight = map(str,input().split(" "))
        weight = int(weight)
        if weight > most_weight:
            most_weight = weight
            most_name = bunny_name
        if weight > 15:
            count += 1
    print(count)
    print(most_name)
main()
