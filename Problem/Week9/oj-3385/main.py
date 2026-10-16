"""docstring module"""
def main():
    """main function"""
    p = int(input())
    n = int(input())
    queues = {}
    for _ in range(n):
        parts = list(map(int, input().split()))
        queues[parts[0]] = parts[1:]
    total_success = 0
    bus_destinations = {}
    current_load = 0
    for current_stop in range(1, n + 1):
        if current_stop in bus_destinations:
            dropped = bus_destinations[current_stop]
            total_success += dropped
            current_load -= dropped
            del bus_destinations[current_stop]
        if current_stop in queues:
            for dest in queues[current_stop]:
                if dest > current_stop:
                    if current_load < p:
                        bus_destinations[dest] = bus_destinations.get(dest, 0) + 1
                        current_load += 1
                    else:
                        break
    print(total_success)
main()
