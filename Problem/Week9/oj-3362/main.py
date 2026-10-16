"""docstirng module"""
def init_names(name1,name2): # step1
    """prepare name to use"""
    names = [name1.lower(),name2.lower()]
    names = sorted(names,key=len)
    new_name = ""
    count = 0
    for _ in names[1]:
        if count >= len(names[0]):
            count = 0
        new_name += names[0][count]
        count += 1
    names[0] = new_name.lower()
    return names
def love_check(names): #step2
    """check if word have 'love' and interpret word"""
    word = ""
    for i in range(len(names[0])):
        if names[0][i] in "love" or names[1][i] in "love":
            word += "w"
        else:
            word += "$"
    return word
def check_w(word): #step3
    """check w in word"""
    longest_w = 0
    all_w = 0
    count = 0
    for i in word:
        all_w += 1 if i == "w" else 0
        count = count+1 if i == "w" else 0
        longest_w = count if count > longest_w else longest_w
    if all_w%2:
        word += str(longest_w)
    else:
        if longest_w < 2:
            word += "#"
    return word
def main():
    """main function"""
    name1 = input()
    name2 = input()
    names = init_names(name1,name2)
    love_word = love_check(names)
    result = check_w(love_word)
    print(result)
main()
