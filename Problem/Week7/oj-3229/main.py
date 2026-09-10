"""score game"""
def key_score_func(score):
    """calculate key"""
    key = 1
    if score < 200:
        key = 1
    elif 200 <= score < 500:
        key = 2
    elif 500 <= score < 1000:
        key = 3
    elif 1000 <= score < 1500:
        key = 4
    elif score >= 1500:
        key = 5
    return key
def main():
    """main function"""
    baseScore = int(input())
    bonusScore = int(input())
    dayStreak = int(input())
    #-Calculate
    totalScore = baseScore+bonusScore
    totalScore *= 1.5 if dayStreak >= 3 else 1
    #-Condition Check
    key = key_score_func(totalScore)
    keySpecial = 0
    keySpecial = 99 if key == 5 and dayStreak >= 7 else keySpecial
    keySpecial = 88 if key == 4 and bonusScore > 300 else keySpecial
    print(int(totalScore))
    print(key)
    print(keySpecial)
main()
