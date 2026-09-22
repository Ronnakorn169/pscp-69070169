"""docstring module"""

def find_longest_a(text):
    """Find A that longest"""
    max_count = 0
    current_count = 0
    for char in text:
        if char == 'a':
            current_count += 1
            if current_count > max_count:
                max_count = current_count
        else:
            current_count = 0
    return max_count

def check_race(text):
    """check the rabbit race"""
    state = "unknown"
    num = 0
    text = list(text)
    for i,v in enumerate(text):
        # check r and a
        if v not in "rabit":
            state = "no"
            num = i
            break
        try:
            if v == "r":
                if i + 1 == len(text) or text[i+1] != "a":
                    state = "no"
                    num = i+1
                    break
                state = "yes"
            if v == "a":
                if not i or text[i-1] not in "ra":
                    state = "no"
                    num = i
                    break
        except IndexError:
            state = "no"
            num = i
        try:
            if v == "b" and text[i+1] not in "it":
                state = "no"
                num = i+1
                break
            if v == "b" and text[i+1] in "it":
                state = "yes"
        except IndexError:
            state = "no"
            num = i
    return (state,num)

def main():
    """main function"""
    text = input().lower()
    state = check_race(text)[0]
    num = check_race(text)[1]
    if state == "yes":
        print("yes",find_longest_a(text))
    elif state == "no":
        print("no",num)
    else:
        print("unknown",len(text))
main()
