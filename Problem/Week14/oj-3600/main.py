"""docstring module"""
def main():
    """main function"""
    list_order = {
        1 : 100,
        2 : 120,
        3 : 200,
        4 : 60,
        5 : -1
    }
    last_input = 0
    result = 0
    while last_input != -1:
        result += last_input
        order = int(input())
        last_input = list_order[order]
    print("Bye Bye")
    print("Total Calories:",result)
main()
