"""docstring module"""
def main():
    """main function"""
    num = int(input())
    if num < 2:
        print("No")
        return

    is_prime = [True] * (num + 1)
    is_prime[0] = False
    is_prime[1] = False

    limit = int(num ** 0.5)
    for base in range(2, limit + 1):
        if is_prime[base]:
            for multiple in range(base * base, num + 1, base):
                is_prime[multiple] = False

    if is_prime[num]:
        print("Yes")
        primes = [i for i in range(2, num + 1) if is_prime[i]]
        print(*primes)
    else:
        print("No")

main()
