"""docstring module"""
def main():
    """main function"""
    n = int(input())
    poles = sorted(int(input()) for _ in range(n))
    total_distance = 0
    current_length = 0
    for p in poles:
        current_length += p
        total_distance += current_length * 2
    print(total_distance)
main()
