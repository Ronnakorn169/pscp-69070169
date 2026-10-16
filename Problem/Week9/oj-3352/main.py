"""LAST STAND"""
import json
def main():
    """main function"""
    list_num = json.loads(input())
    for num in list_num:
        print(str(num)[-1])
main()
