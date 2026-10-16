"""docstring module"""
def main():
    """main function"""
    n, start = map(int,input().split())
    sent_list = [0]
    sent_list += list(map(int,[input() for _ in range(n)]))
    already_sent = set()
    stopLoop = False
    total_sent = 0
    while not stopLoop:
        if start in already_sent or not start:
            stopLoop = True
            break
        total_sent += 1
        already_sent.add(start)
        start = sent_list[start]
    print(total_sent)
main()
