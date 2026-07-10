"""docstring module"""
def main():
    """main function"""
    input_menu = input()
    #/
    carrot = int(input_menu.split(" ")[0])
    cabbage = int(input_menu.split(" ")[1])
    tometo = int(input_menu.split(" ")[2])
    #/
    calculate = (carrot*10) + (cabbage*25) + (tometo*3)
    print(calculate)
main()
