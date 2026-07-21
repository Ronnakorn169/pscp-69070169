"""docstring module"""
def main():
    """main func"""
    r,x,y = map(int,input().split(" "))
    eye = (x**2)+(y**2)
    size = r**2
    if eye == size:
        print("ON")
    elif eye < size:
        print("IN")
    else:
        print("OUT")
main()
