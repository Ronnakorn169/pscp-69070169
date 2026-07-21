"""docstring module"""
def main():
    """main func"""
    r,h,glue = map(float,input().split(" "))
    length = (2 * 3.14 * r) + glue
    width = h + (2 * r)
    print(f"{width:.2f} {length:.2f}")
main()
