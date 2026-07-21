"""docstring module"""
def main():
    """main func"""
    student = int(input())
    top_score = 0
    top_score_student = 0
    for _ in range(student):
        score = int(input())
        if score >= top_score:
            if score == top_score:
                top_score_student += 1
            else:
                top_score_student = 1
            top_score = score
    print(top_score)
    print(top_score_student)
main()
