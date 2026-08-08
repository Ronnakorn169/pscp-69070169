"""docstring module"""
def main():
    """main function"""
    size,soup_type = map(str,input().split(" "))
    topping = input()
    topping_dict = {
        "N" : 0,
        "P" : 15,
        "E" : 10
    }
    ramen_dict = {
        ("S","R") : 60,
        ("S","T") : 80,
        #/
        ("M","R") : 80,
        ("M","T") : 100,
        #/
        ("L","R") : 100,
        ("L","T") : 120,
    }
    topping_multiply = 1
    if len(topping.split(" ")) > 1:
        topping_multiply = int(topping.split(" ")[1])
    result = ramen_dict[(size,soup_type)] + topping_dict[topping.split(" ")[0]] * topping_multiply
    print(result)
main()
