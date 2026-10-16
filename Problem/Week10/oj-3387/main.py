"""docstring module"""
def main():
    """main function"""
    num_tuple = tuple(input().split(" "))
    num_find = input()
    index_find = num_tuple.index(num_find)
    size = num_tuple.count(num_find)
    for _ in range(size):
        print(" ".join([str(index_find)] * size))
main()
