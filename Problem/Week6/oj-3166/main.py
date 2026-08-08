"""docstring module"""
def main():
    """main function"""
    n = int(input())
    all_score = []
    ispass = True
    for _ in range(n):
        score = float(input())
        all_score.append(score)
        if score < 50:
            ispass = False
    avg_score = sum(all_score)/n
    ispass = False if avg_score < 60 else ispass
    print(f"{avg_score:.1f}")
    if ispass:
        print("PASS")
    else:
        print("FAIL")
main()
