"""mix color"""
def mix(rgb1,rgb2,t):
    """calculate gradient"""
    newrgb = []
    for i in range(0,3):
        c1 = (rgb1[i]/255)*t
        c2 = (rgb2[i]/255)*t
        result = int((c1+c2)*255)
        newrgb.append(result)
    return newrgb
def main():
    """main function"""
    rgb1 = list(map(int,input().split(" ")))
    rgb2 = list(map(int,input().split(" ")))
    newrgb = mix(rgb1,rgb2,0.5)
    for i in newrgb:
        print(i,end=" ")
main()
