"""docstring module"""
def main():
    """main function"""
    num_limit = int(input())
    seen = set()
    while True:
        val = int(input())
        if not val:
            break
        seen.add(val)
    for num in range(1, num_limit + 1):
        if num not in seen:
            print(num)
main()
