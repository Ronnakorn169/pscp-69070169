"""docstring module"""
def main():
    """main function"""
    n = int(input())
    pigs = list(map(int,input().split(" ")))
    pigs_sort = []
    for i in range(0,n*2,2):
        pigs_sort.append(max(pigs[i],pigs[i+1]))
    # OUTPUT
    for i,v in enumerate(pigs_sort):
        print(v,end="")
        if i != len(pigs_sort)-1:
            print(" + ",end="")
        elif len(pigs_sort) > 1:
            print(" =",sum(pigs_sort))
main()
