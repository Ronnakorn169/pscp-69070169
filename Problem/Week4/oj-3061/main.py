"""docstring module"""
def main():
    """main function"""
    mid_score = int(input())
    final_score = int(input())
    sum_score = mid_score+final_score
    print(sum_score)
    if sum_score >= 50:
        print("pass")
    else:
        print("fail")
main()
