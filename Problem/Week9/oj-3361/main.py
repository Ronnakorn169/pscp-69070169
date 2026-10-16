"""docstring module"""
def main():
    """main function"""
    n = int(input())
    list_cars = []
    result = 0
    for _ in range(n):
        car_info = list(map(int,input().split(" ")))
        list_cars.append(car_info)
    list_cars = sorted(list_cars,key=lambda x:x[0])
    max_v = list_cars[0]
    for i in range(1,len(list_cars)):
        if max_v[1] > list_cars[i][1]:
            result += 1
        else:
            max_v = list_cars[i]
    print(result)
main()
