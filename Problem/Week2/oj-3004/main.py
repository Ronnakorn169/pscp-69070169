"""docstring module"""
import math
def main():
    """main function"""
    input_pos1 = input()
    input_pos2 = input()
    #/ Pos1
    x1 = int(input_pos1.split(" ")[0])
    y1 = int(input_pos1.split(" ")[1])
    z1 = int(input_pos1.split(" ")[2])
    #/ Pos2
    x2 = int(input_pos2.split(" ")[0])
    y2 = int(input_pos2.split(" ")[1])
    z2 = int(input_pos2.split(" ")[2])
    #/ Calculate
    d = math.sqrt( ((x1-x2)**2)+((y1-y2)**2)+((z1-z2)**2)  )
    if d%1:
        print(f"{d:.2f}")
    else:
        print(f"{int(d)}")
main()
