"""docstring module"""
def calculate_area(x,y):
    """calculate area"""
    return x*y
def main():
    """main function"""
    width, height, xAmount, yAmount = map(int,input().split(" "))
    x_pos = list(map(int,input().split(" ")))
    y_pos = list(map(int,input().split(" ")))
    x_pos.append(width)
    y_pos.append(height)
    dx = []
    for i in range(xAmount + 1):
        prev_x = x_pos[i-1] if i else 0
        dx.append(x_pos[i] - prev_x)
    dy = []
    for j in range(yAmount + 1):
        prev_y = y_pos[j-1] if j else 0
        dy.append(y_pos[j] - prev_y)
    dx = sorted(dx, reverse=True)[:2]
    dy = sorted(dy, reverse=True)[:2]
    areas = []
    for i in dx:
        for j in dy:
            area = calculate_area(i,j)
            areas.append(area)
    areas = sorted(areas,reverse=True)
    print(areas[0],areas[1])
main()
