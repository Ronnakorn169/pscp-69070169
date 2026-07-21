"""docstring module"""
import math
def main():
    """main func"""
    pushup_req = int(input())
    situp_req = int(input())
    squat_req = int(input())
    run_req = int(input())
    #/
    pushup_per_day = int(input())
    situp_per_day = int(input())
    run_per_day = int(input())
    squat_per_day = int(input())
    #/
    max_pushup_day = math.ceil(pushup_req/pushup_per_day)
    max_situp_day = math.ceil(situp_req/situp_per_day)
    max_squat_day = math.ceil(squat_req/squat_per_day)
    max_run_day = math.ceil(run_req/run_per_day)
    #/
    day_need = max(max_pushup_day,max_situp_day,\
                   max_squat_day,max_run_day)
    print(day_need)
main()
