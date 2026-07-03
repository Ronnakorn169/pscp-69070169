"""module"""
def main():
    "main"
    color1 = input()
    color2 = input()
    if color1 not in ["Red","Yellow","Blue"]:
        print("Error")
        return
    if color2 not in ["Red","Yellow","Blue"]:
        print("Error")
        return
    if color1 != color2:
        ListRed = {"Orange","Violet"}
        ListBlue = {"Violet","Green"}
        ListYellow = {"Green","Orange"}
        DictColor = {
            "Red":ListRed,
            "Yellow":ListYellow,
            "Blue":ListBlue}
        intersectColor = DictColor[color1] & DictColor[color2]
        for item in intersectColor:
            print(item)
    else:
        print(color1)
main()
