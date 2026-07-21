"""docstring module"""
import math
def main():
    """main func"""
    delta_Area,people = map(int,input().split(" "))
    for _ in range(people):
        x,y = map(float,input().split(" "))
        r = math.sqrt((x**2)+(y**2))
        Area = (r**2)*3.1416
        Time = Area/delta_Area
        print(math.ceil(Time))
main()
