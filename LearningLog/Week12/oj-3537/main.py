"""docstring module"""
def main():
    """main function"""
    alive = {}
    while True:
        line = input().strip()
        if line == "Start":
            break
        clean = line.strip("{}").split(":")
        name = clean[0].strip().strip("\"'")
        role = clean[1].strip().strip("\"'")
        alive[name] = role

    dead = {}
    while True:
        line = input().strip()
        if line == "End":
            break
        if line in alive:
            dead[line] = alive.pop(line)

    impostor_count = list(alive.values()).count("Impostor")
    print(f"{impostor_count} Impostor Remains")
    print("***Alive***")
    for name in sorted(alive):
        print(f"{name} : {alive[name]}")
    print("***Dead***")
    for name in sorted(dead):
        print(f"{name} : {dead[name]}")

main()
