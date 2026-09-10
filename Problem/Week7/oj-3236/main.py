"""docstring"""
def main():
    """main"""
    length = int(input())
    sID_1 = input()
    sID_2 = input()
    total_wrong = 0
    for i in range(length):
        if int(sID_1[i]) + int(sID_2[i]) != 9:
            total_wrong += 1
    result = "YES" if not total_wrong else "NO "+str(total_wrong)
    print(result)
main()
