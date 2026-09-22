"""docstring module"""
def calculate_space_left(w,l,a):
    """calculate space left function"""
    area1 = (w // a) * l
    area2 = (w % a) * (l // a)
    return (w*l)-((area1 + area2)*a)
def main():
    """main function"""
    W , L , M , N = map(int,input().split(" "))
    lowest = 0
    for i in range(M,N+1):
        space_left = calculate_space_left(W,L,i)
        if i == M:
            lowest = space_left
        lowest = space_left if space_left < lowest else lowest
    print(lowest)
main()
