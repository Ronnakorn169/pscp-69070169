"""docstring"""
def main():
    """main"""
    colorStart , quantity = map(str,input().split(" "))
    rgb = ["Red","Green","Blue"]
    index = next(i for i,v in enumerate(rgb) if v.startswith(colorStart,None))
    for _ in range(int(quantity)):
        print(rgb[index],end=" ")
        index += 1
        index = 0 if index > 2 else index
main()
