"""docstring module"""
def main():
    """main function"""
    day = int(input())
    month = int(input())
    sign = ""
    if month == 1:
        sign = "capricorn" if (day < 20) else "aquarius"
    elif month == 2:
        sign = "aquarius" if (day < 19) else "pisces"
    elif month == 3:
        sign = "pisces" if (day < 21) else "aries"
    elif month == 4:
        sign = "aries" if (day < 20) else "taurus"
    elif month == 5:
        sign = "taurus" if (day < 21) else "gemini"
    elif month == 6:
        sign = "gemini" if (day < 21) else "cancer"
    elif month == 7:
        sign = "cancer" if (day < 23) else "leo"
    elif month == 8:
        sign = "leo" if (day < 23) else "virgo"
    elif month == 9:
        sign = "virgo" if (day < 23) else "libra"
    elif month == 10:
        sign = "libra" if (day < 23) else "scorpio"
    elif month == 11:
        sign = "scorpio" if (day < 22) else "sagittarius"
    elif month == 12:
        sign = "sagittarius" if (day < 22) else "capricorn"
    print(sign)
main()
