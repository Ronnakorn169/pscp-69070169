"""docstring module"""
def main():
    """main function"""
    n = int(input())
    list_sort = []
    for _ in range(n):
        amount = int(input())
        list_num = []
        for _ in range(amount):
            list_num.append(list(map(int,input().split(" "))))
        list_num = sorted(list_num,key=lambda x: ( x[0]+x[1] , x[0]) )
        list_sort.append(list_num)
    for i in list_sort:
        for j in i:
            print(" ".join(str(x) for x in j))
main()
