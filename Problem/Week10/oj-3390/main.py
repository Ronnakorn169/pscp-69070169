"""docstring module"""
def main():
    """main function"""
    arrays = []
    for _ in range(5):
        arr = list(map(int, input().split()))
        arrays.append(arr)
    index_row = -1
    index_col = -1
    for i in range(5):
        if sum(arrays[i]) % 2:
            index_row = i
        total = 0
        for j in range(5):
            total += arrays[j][i]
        if total % 2:
            index_col = i
    print(f"{index_row} {index_col}")
main()
