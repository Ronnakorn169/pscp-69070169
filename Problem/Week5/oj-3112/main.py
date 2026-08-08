"""docstring module"""
def main():
    """main function"""
    boba_type,boba_quantity = map(str,input().split(" "))
    boba_quantity = float(boba_quantity)
    tea_type,level_sweat,tea_quantity = map(str,input().split(" "))
    tea_quantity = float(tea_quantity)
    level_sweat = int(level_sweat)
    tea_dict = {
        #/R
        ("R",1) : 12,
        ("R",2) : 18,
        ("R",3) : 25,
        #/T
        ("T",1) : 15,
        ("T",2) : 20,
        ("T",3) : 30,
        #/M
        ("M",1) : 10,
        ("M",2) : 15,
        ("M",3) : 20,
    }
    boba_dict = {
        "H" : 5,
        "O" : 3,
        "J" : 2
    }
    result = boba_dict[boba_type]*boba_quantity + \
          tea_dict[(tea_type,level_sweat)]*tea_quantity
    if result % 1:
        print(f"{result}")
    else:
        print(f"{int(result)}")
main()
