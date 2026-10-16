"""docstring module"""
def shorten_num(num_list):
    """shorten number function"""
    num_list = sorted(num_list)
    outputList = []
    lastNum = 0
    isContinue = False
    for i,num in enumerate(num_list):
        if not i:
            lastNum = num
            continue
        if num_list[i-1]+1 == num:
            isContinue = True
            continue
        if num_list[i-1]+1 != num:
            if isContinue:
                outputList.append(f"{lastNum}-{num_list[i-1]}")
            else:
                outputList.append(f"{num_list[i-1]}")
            lastNum = num
            isContinue = False
    if isContinue:
        outputList.append(f"{lastNum}-{num_list[-1]}")
    else:
        outputList.append(f"{num_list[-1]}")
    return outputList
def main():
    """main function"""
    numList = []
    input_num = 0
    while input_num != -1:
        input_num = int(input())
        if input_num != -1:
            numList.append(input_num)
    if len(numList) > 0:
        outputList = shorten_num(numList)
        for i,v in enumerate(outputList):
            if i+1 != len(outputList):
                print(v,end=", ")
            else:
                print(v)
main()
