"""docstirng module"""
def main():
    """main function"""
    n = int(input())
    giraffs = []
    count = 0
    for _ in range(n):
        giraffs.append(int(input()))
    for i,v in enumerate(giraffs):
        left = giraffs[max(0,i-1)]
        right = giraffs[min(len(giraffs)-1,i+1)]
        is_happy = True
        if (left >= v and i) or (right >= v and i != len(giraffs)-1):
            is_happy = False
        count += 1 if is_happy else 0
    print(count)
main()
