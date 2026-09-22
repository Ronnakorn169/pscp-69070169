"""bunny BUU"""
def check_main(text):
    """check1"""
    count = 0
    isStartCounting = False
    longest = 0
    for i in text:
        if i == "b" and not isStartCounting:
            isStartCounting = True
        elif i == "u" and isStartCounting:
            count += 1
        elif isStartCounting:
            if i == "b":
                count = 0
            else:
                isStartCounting = False
        longest = count if count > longest else longest
    print("Yes",longest)
def check2(text):
    """check 2 - if b in text"""
    indexB = str(text).find("b")
    if indexB == -1:
        indexB = str(text).find("B")
    print(text[0:indexB+1]+"U"*(len(text)-(indexB+1)))
def check3(text):
    """if no B then replace BUU"""
    new_text = ""
    check = ""
    for _ in text:
        if check != "BUU":
            if check:
                check += "U"
                new_text += "U"
            else:
                check += "B"
                new_text += "B"
        else:
            check = "B"
            new_text += "B"
    print(new_text)
def main():
    """main function"""
    text = input()
    t = text.lower()
    if "buu" in t:
        check_main(t)
    else:
        if "b" in text or "B" in text:
            check2(text)
        else:
            check3(text)
main()
