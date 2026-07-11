"""docstring module"""
def main():
    """main function"""
    month = float(input())
    day = int(input())
    #/
    season = {1:"winter",
              2:"spring",
              3:"summer",
              4:"fall"}
    index_season = int(((month-1)//3)+1)
    if not month%3 and day >= 21:
        index_season+=1
    if index_season > 4:
        index_season = 1
    print(season[index_season])
main()
