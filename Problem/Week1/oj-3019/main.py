"""module"""
PASSWORD = "H 4567"
def main():
    """main"""
    input_char = input()
    input_num = int(input())
    lockedstate = {
        (False,False):"safe unlocked",
        (True,False):"safe locked - change digit",
        (False,True):"safe locked - change char",
        (True,True):"safe locked"
    }
    current_state = [False,False]
    if input_char != PASSWORD.split(" ", maxsplit=1)[0]:
        current_state[1] = True
    if str(input_num) != PASSWORD.split(" ", maxsplit=1)[1]:
        current_state[0] = True
    print(lockedstate[tuple(current_state)])
main()
