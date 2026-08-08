"""docstring module"""
def main():
    """main function"""
    dict_key = {
        ("BKK","CNX") : (10,30),
        ("CNX","UBP") : (15,40),
        ("UBP","BKK") : (20,40),
        ("BKK","PKT") : (25,50),
        ("PKT","CNX") : (30,60),
        ("UBP","PKT") : (40,70),
    }
    station = tuple(input().upper().split(" "))
    weight_package = float(input())
    try:
        tax_start = dict_key[station][0]
        tax_per_kk = dict_key[station][1]
        result = tax_start+(weight_package*tax_per_kk)
        print(f"{result:.2f}")
    except KeyError:
        print("Error")
main()
