"""ijudge"""
def star_check(number):
    """check start function"""
    if number == '1':
        print("1 STAR")
    elif number == "2":
        print("2 STAR")
    elif number == "3":
        print("3 STAR")
    elif number == "0":
        print("0 STAR")
    else:
        print("INVALID")
MAIN_CHECK_TEXT = "https://ijudge.it.kmitl.ac.th/problems/"
def main():
    """main function"""
    text = input()
    text_count_main = len(MAIN_CHECK_TEXT)
    for i in range(text_count_main):
        if text[i] != MAIN_CHECK_TEXT[i]:
            print("INVALID")
            return
    text2 = text.split(MAIN_CHECK_TEXT)
    if len(text2[1]) == 4 or len(text2[1]) == 5:
        textcheck = text2[1]
        if len(text2[1]) == 5:
            textcheck = text2[1][:4]
        for i in textcheck:
            if i not in "0123456789":
                print("INVALID")
                return
        number = text2[1][0]
        star_check(number)
    else:
        print("INVALID")
main()
