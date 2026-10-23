"""docstring module"""
def main():
    """main function"""
    num_a = int(input())
    num_b = int(input())
    while num_b:
        num_a, num_b = num_b, num_a % num_b
    print(abs(num_a))
main()
