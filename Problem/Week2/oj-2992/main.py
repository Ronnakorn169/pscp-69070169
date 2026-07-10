"""docstring module"""
def main():
    """main function"""
    num_input = input()
    operator_input = input()
    #/
    num_origin = int(num_input)
    num_reverse = int(num_input[::-1])
    result = 0
    match(operator_input):
        case "+":
            result = num_origin+num_reverse
        case "-":
            result = num_origin-num_reverse
        case "*":
            result = num_origin*num_reverse
        case "/":
            result = num_origin/num_reverse
    print(f"{num_origin} {operator_input} {num_reverse} = {result}")
main()
