"""Bonus"""
def main():
    """Bonus"""
    pos, years, salary = input().split()
    years = int(years)
    salary = float(salary)
    fixed = {'M': 1500, 'B': 1000, 'G': 500}
    rate = {
        'M': (6, 8, 10),
        'B': (5, 6, 7),
        'G': (4, 5, 6)
    }
    if years <= 5:
        pct = rate[pos][0]
    elif years <= 10:
        pct = rate[pos][1]
    else:
        pct = rate[pos][2]
    bonus = fixed[pos] + salary * pct / 100
    print(int(bonus))
main()
