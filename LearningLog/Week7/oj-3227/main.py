"""docstring module"""
def main():
    """main function"""
    text = input().upper()
    upperScoreCards = {
        "A":"ace",
        "J":"jack",
        "Q":"queen",
        "K":"king"
    }
    groupCards = {
        "D":"diamonds",
        "H":"hearts",
        "S":"spades",
        "C":"clubs"
    }
    groupKey = text[-1:]
    score = text[-2::-1][::-1]

    score = upperScoreCards.get(score, score)
    print(score,"of",groupCards[groupKey])
main()
