"""docstring module"""
def main():
    """main function"""
    cave_size = int(input())
    cave_map = list(map(int,input().split()))
    command = input()
    cur_pos = cave_map.index(1)
    for i in command:
        cave_map[cur_pos] = 0
        cur_pos += 1 if i == "R" else -1
        #border check--------
        cur_pos = cave_size-1 if cur_pos >= cave_size else cur_pos
        cur_pos = 0 if cur_pos < 0 else cur_pos
        #--------------------
        cave_map[cur_pos] = 1
        if cave_map[cur_pos] == 2:
            break
    print(" ".join(map(str,cave_map)))
main()
