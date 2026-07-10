"""docstring module"""
def main():
    """main function"""
    input1 = input()
    input_price = int(input())
    #/
    width = int(input1.split(" ")[0])
    length = int(input1.split(" ")[1])
    wall_height = int(input1.split(" ")[2])
    #/
    area = ((width*2)+(length*2))* wall_height
    price = (area) * input_price
    print(area)
    print(price)
main()
