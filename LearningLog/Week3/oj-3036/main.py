"""docstring module"""
import math
def next_room_func(n):
    """Calculate Next Room"""
    floor = math.ceil(math.sqrt(n))
    room = n - (floor-1)**2
    #/
    upper_room = 0
    nextroom = 0
    if not room % 2:
        upper_room = room-1
        nextroom = ((floor-2)**2) + upper_room
    else:
        if room > 1:
            upper_room = room-1
            nextroom = ((floor-1)**2) + upper_room
        else:
            nextroom =  ((floor-1)**2) + (room+1)
    return nextroom
def main():
    """main func"""
    n = int(input())
    #/
    current_room = n
    amount_mining = 0
    while current_room != 1:
        current_room = next_room_func(current_room)
        amount_mining += 1
    print(amount_mining)
main()
