"""docstring"""
#matrix method
#https://hub.paper-checker.com/blog/efficient-fibonacci-calculating-the-nth-number-in-olog-n/
#i just copy this
def multiply(f,m):
    """multiply matrix"""
    x = f[0][0] * m[0][0] + f[0][1] * m[1][0]
    y = f[0][0] * m[0][1] + f[0][1] * m[1][1]
    z = f[1][0] * m[0][0] + f[1][1] * m[1][0]
    w = f[1][0] * m[0][1] + f[1][1] * m[1][1]
    f[0][0] = x
    f[0][1] = y
    f[1][0] = z
    f[1][1] = w
    return f
def power(f, n):
    """power matrix"""
    if n <= 1 :
        return n
    m = [[1, 1], [1, 0]]
    power(f, n // 2)
    multiply(f, f)
    if n % 2 :
        multiply(f, m)
    return 0
def fibonacci(n):
    """fibonacci"""
    if not n :
        return 0
    f = [[1, 1], [1, 0]]
    power(f, n - 1)
    return f[0][0]
def main():
    """main function"""
    num_input = int(input())
    print(fibonacci(num_input))
main()
