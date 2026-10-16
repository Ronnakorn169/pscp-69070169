"""docstring module"""
def get_candidates(x, y, d):
    """find candidate points on circle"""
    pts = set()
    d2 = d * d
    for dx in range(-d, d + 1):
        rem = d2 - dx * dx
        dy = int(rem ** 0.5)
        if dy * dy == rem:
            for ny in (y - dy, y + dy):
                nx = x + dx
                if 0 <= nx <= 1000 and 0 <= ny <= 1000:
                    pts.add((nx, ny))
    return pts
def match_shot(tx, ty, shots):
    """check if target matches all shots"""
    euc = all((tx - x) ** 2 + (ty - y) ** 2 == d * d for x, y, d in shots)
    rnd = all(int(((tx - x) ** 2 + (ty - y) ** 2) ** 0.5 + 0.5) == int(d) for x, y, d in shots)
    man = all(abs(tx - x) + abs(ty - y) == d for x, y, d in shots)
    return euc or rnd or man
def main():
    """main function"""
    n = int(input())
    shots = [list(map(float, input().split())) for _ in range(n)]
    x0, y0, d0 = [int(v) for v in shots[0]]
    cands = get_candidates(x0, y0, d0)
    for tx, ty in sorted(cands):
        if all((tx - int(x)) ** 2 + (ty - int(y)) ** 2 == int(d) ** 2 for x, y, d in shots):
            print(f"{tx} {ty}")
            return
    for tx in range(1001):
        for ty in range(1001):
            if match_shot(tx, ty, shots):
                print(f"{tx} {ty}")
                return
main()
