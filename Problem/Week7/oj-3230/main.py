"""roam find room"""
import math
def decode_firstkey_func(encode_num):
    """find first key (floor)"""
    numTable = {
        0:"9",
        1:"10",
        2:"11",
        3:"12",
        4:"14",
        -1:"13"
    }
    for i,v in enumerate(encode_num):
        if int(v) > 5:
            return numTable[i]
    return numTable[-1]
def decode_second_key(encode_num):
    "find 2nd key (room)"
    #Palindrome
    if encode_num == encode_num[::-1]:
        if int(encode_num[0]) + int(encode_num[4]) > 5:
            return "1"
        if int(encode_num[1]) * int(encode_num[3]) > 5:
            return "2"
    else:
        if int(encode_num[4]) and math.ceil(int(encode_num[0]) / int(encode_num[4])) > 5:
            return "1"
        if int(encode_num[1]) - int(encode_num[4]) > 5:
            return "2"
    return "0"
def decode_third_key(encode_num):
    """find 3rd key (room)"""
    totalSumNum = 0
    totalMultiplyNum = 1
    for i in encode_num:
        totalSumNum += int(i)
        totalMultiplyNum *= int(i)
    if totalSumNum > 25:
        return "1"
    if totalMultiplyNum > 55:
        return "2"
    return "0"
def decode_key(encode_num):
    """GET KEY"""
    Key = ""
    Key = \
    decode_firstkey_func(encode_num) + \
    decode_second_key(encode_num) + \
    decode_third_key(encode_num)
    return Key
def main():
    """main function"""
    encodeNum = input()
    print(decode_key(encodeNum))
main()
