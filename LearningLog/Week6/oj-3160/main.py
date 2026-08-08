"""docstring module"""
def main():
    """main function"""
    start,end = map(int,input().split(" "))
    prime_number = []
    for i in range(start,end+1):
        if i == 1 or not i:
            continue
        isprime = True
        for j in range(2,i):
            if not i%j:
                isprime = False
        if isprime:
            prime_number.append(i)
    member_count = len(prime_number)
    for i in range(member_count):
        if i != len(prime_number)-1:
            print(prime_number[i],end=" ")
        else:
            print(prime_number[i])
    print("Total primes:",len(prime_number))
main()
