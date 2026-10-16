"""docstring module"""
def main():
    """main function"""
    first_line = input().split()
    n = int(first_line[0])
    p = float(first_line[1])
    grid = [list(map(int, input().split())) for _ in range(n)]
    total_tiles = 0
    total_spots = 0
    for row in grid:
        row_tiles = sum(1 for x in row if x > 0)
        row_spots = sum(row)
        total_tiles += row_tiles
        total_spots += row_spots
        print(*row, row_tiles, row_spots)
    col_tiles = [sum(1 for r in range(n) if grid[r][c] > 0) for c in range(n)]
    col_spots = [sum(grid[r][c] for r in range(n)) for c in range(n)]
    print(*col_tiles)
    print(*col_spots)
    print(f"{total_tiles} {total_spots} {total_spots * p:.2f}")
main()
