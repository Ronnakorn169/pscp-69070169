"""docstring module"""
def main():
    """docstring main"""
    xA_BottomLeft,yA_BottomLeft,wA,hA = map(int,input().split(" "))
    xB_BottomLeft,yB_BottomLeft,wB,hB = map(int,input().split(" "))
    #/
    overlap_left = max(xA_BottomLeft, xB_BottomLeft)
    overlap_right = min(xA_BottomLeft+wA, xB_BottomLeft+wB)
    overlap_bottom = max(yA_BottomLeft, yB_BottomLeft)
    overlap_top = min(yA_BottomLeft+hA, yB_BottomLeft+hB)
    #/
    overlap_width = overlap_right - overlap_left
    overlap_height = overlap_top - overlap_bottom
    if overlap_width > 0 and overlap_height > 0:
        print(overlap_width * overlap_height)
    else:
        print("no overlapping")
main()
