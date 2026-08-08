"""docstring module"""
import math
def main():
    """main function"""
    position , year_service , salary = map(str,input().split())
    bonus_pos = {"M":1500,"B":1000,"G":500}
    bonus_percent = {("M",0):.06,
                     ("M",1):.08,
                     ("M",2):.1,
                     ("B",0):.05,
                     ("B",1):.06,
                     ("B",2):.07,
                     ("G",0):.04,
                     ("G",1):.05,
                     ("G",2):.06,
                     }
    year_service = math.ceil(float(year_service))
    if year_service < 5:
        year = 0
    elif 5 <= year_service <= 10:
        year = 1
    else:
        year = 2
    salary = float(salary)
    bonus_per = bonus_percent[(position,year)]
    bonus_result = salary*bonus_per+bonus_pos[position]
    print(f"{int(bonus_result)}")
main()
