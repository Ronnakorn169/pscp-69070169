"""docstring module"""
def main():
    """main function"""
    n, m = map(int, input().split())
    if 1 <= n <= 10 and 1 <= m <= 20:
        grid = [list(map(int, input().split())) for _ in range(n)]
        valid = all(len(row) == m and all(0 <= x <= 100 for x in row) for row in grid)
        if valid:
            total_sum = 0
            for idx, row in enumerate(grid, 1):
                row_sum = sum(row)
                total_sum += row_sum
                print(f"Team {idx}: Average = {row_sum / m:.2f}, Max = {max(row)}")
            print(f"Total Score of All Teams = {total_sum}")
        else:
            print("Data Incorrect")
    else:
        print("Data Incorrect")
main()
