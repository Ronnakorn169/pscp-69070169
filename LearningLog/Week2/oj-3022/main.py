"""docstring module"""
def to_celcius(temp,temp_type):
    """function that cal to celcius"""
    result = 0
    match(temp_type):
        case "K":
            result = temp-273.15
        case "F":
            result = (temp-32) * 5/9
        case "R":
            result = (temp-491.67)*5/9
        case "C":
            result = temp
    return result

def main():
    """main"""
    temp1 = float(input())
    temp_type = input()
    type_want = input()
    #/
    cel_temp = to_celcius(temp1,temp_type)
    result = cel_temp
    match type_want:
        case "C":
            result = cel_temp
        case "K":
            result = cel_temp+273.15
        case "F":
            result = (cel_temp * 9/5) +32
        case "R":
            result = (cel_temp + 273.15)* 9 / 5
    print(f"{result:.2f}")
main()
