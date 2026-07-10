"""docstring module"""
def main():
    """function main"""
    x = int(input())
    y = int(input())
    #/
    quadrant = {(0,0):"O",
                (1,1):"Q1",
                (-1,1):"Q2",
                (-1,-1):"Q3",
                (1,-1):"Q4",
                (0,1):"Y",
                (1,0):"X",
                (0,-1):"Y",
                (-1,0):"X"}
    #/
    if x:
        if x >= 1:
            x = 1
        else:
            x = -1
    if y:
        if y >= 1:
            y = 1
        else:
            y = -1
    vector_norm = (x,y)
    print(quadrant[vector_norm])
main()
