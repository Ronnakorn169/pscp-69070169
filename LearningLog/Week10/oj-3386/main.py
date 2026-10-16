"""docstring module"""
def main():
    """main function"""
    m = int(input())
    n = int(input())
    list1 = set(input() for _ in range(m))
    list2 = set(input() for _ in range(n))
    list_intersect = sorted(list1.intersection(list2),reverse=True)
    if list_intersect:
        print("\n".join(list_intersect))
    else:
        print("Nope")
main()
