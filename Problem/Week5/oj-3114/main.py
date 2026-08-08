"""docstring module"""
import math
def main():
    """main function"""
    start = input()
    end = input()
    start_h,start_m = map(int,start.split("."))
    end_h,end_m = map(int,end.split("."))
    start_h += 1
    end_h += 1
    if start_h > 25 or end_h > 25 or start_m >= 60 or end_m >= 60:
        print("ERROR")
        return
    hour_diff = math.ceil(abs((start_h*60+start_m)-(end_h*60+end_m))/60)
    min_diff = abs((start_h*60+start_m)-(end_h*60+end_m))
    #/
    start_total = (start_h * 60) + start_m
    end_total = (end_h * 60) + end_m
    diff = end_total - start_total
    if diff < 0:
        print("ERROR")
        return
    #/
    if min_diff <= 15:
        print("FREE")
        return
    hour_diff = 7 if 7 <= hour_diff <= 24 else hour_diff
    price_dict = {
        1 : 25,
        2 : 50,
        3 : 80,
        4 : 110,
        5 : 145,
        6 : 180,
        7 : 250
    }
    try:
        print(price_dict[hour_diff])
    except KeyError:
        print("ERROR")
main()
