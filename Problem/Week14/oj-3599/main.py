"""docstring module"""
def main():
    """main function"""
    expect_value = int(input())
    last_input = 0
    result = 0
    try:
        while last_input != -1 and result != expect_value:
            result += last_input
            last_input = int(input())
    except EOFError:
        pass
    print(result)
main()
