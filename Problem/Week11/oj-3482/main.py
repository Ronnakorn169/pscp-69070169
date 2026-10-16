"""docstring module"""
def main():
    """main function"""
    demons = [
        ("Spider Demon", 1),
        ("Swamp Demon", 2),
        ("Arrow Demon", 1),
        ("Hand Demon", 2),
        ("Drum Demon", 3),
        ("Mugen Train", 2),
        ("Upper Moon", 3)
    ]
    kills = 0
    total_attacks = 0
    while kills < 5:
        name, target = demons.pop(0)
        print(name)
        killed = False
        for _ in range(2):
            a = int(input())
            total_attacks += 1
            if a == target:
                print("kill")
                kills += 1
                killed = True
                break
        if not killed:
            print("back")
            demons.append((name, target))
    print(total_attacks)
main()
