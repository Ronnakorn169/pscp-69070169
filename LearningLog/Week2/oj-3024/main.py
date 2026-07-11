"""docstring module"""
def main():
    """main function"""
    avg_score = float(input())
    max_score = float(input())
    #/
    most_min_possible = avg_score - (max_score * 2)
    if most_min_possible < 0:
        most_min_possible = 0
    diff = max_score - most_min_possible
    if diff > 2:
        print("Surprising")
    else:
        print("Not surprising")
main()
