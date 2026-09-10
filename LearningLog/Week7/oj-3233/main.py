"""docstring"""
def check_reward_letter(lottery_num,my_lotter_num):
    """check reward for the letter"""
    if my_lotter_num == lottery_num:
        return 100000
    if my_lotter_num[2:] == lottery_num[2:]:
        return 2000
    if my_lotter_num[3:] == lottery_num[3:]:
        return 1000
    return 20
def check_reward_nonletter(lottery_num,my_lotter_num):
    """check reward for the non-letter"""
    if my_lotter_num == lottery_num:
        return 100000
    if my_lotter_num[2:] == lottery_num[2:]:
        return 200
    if my_lotter_num[3:] == lottery_num[3:]:
        return 100
    return 0
def main():
    """main"""
    lotteryLetter , lotteryNumber = map(str,input().split(" "))
    myLL , myLN = map(str,input().split(" ")) # MyLotteryLetter , MyLotteryNumber
    if myLL == lotteryLetter and myLN == lotteryNumber:
        print(1000000)
    elif myLL == lotteryLetter:
        print(check_reward_letter(lottery_num=lotteryNumber,my_lotter_num=myLN))
    elif myLL != lotteryLetter:
        print(check_reward_nonletter(lottery_num=lotteryNumber,my_lotter_num=myLN))
    else:
        print(0)
main()
