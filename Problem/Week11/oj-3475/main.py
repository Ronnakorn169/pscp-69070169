"""docstring module"""
def main():
    """docstring module"""
    menu = []
    while True:
        try:
            s = input().strip()
            if s == "DONE":
                break
            if s == "CLOSED":
                menu.clear()
                break
            if s == "SOMETHING'S WRONG":
                menu.clear()
            elif s.startswith("Can't do: "):
                item = s[10:]
                while item in menu:
                    menu.remove(item)
            else:
                p = s.rsplit(" #", 1)
                if len(p) == 2:
                    if p[1] == "N":
                        menu.append(p[0])
                    else:
                        menu.insert(int(p[1]) - 1, p[0])
        except EOFError:
            break
    print(f"Full Course: {menu} Reversed: {menu[::-1]}")
main()
