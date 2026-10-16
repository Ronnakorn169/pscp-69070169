"""docstring module"""
def main():
    """main function"""
    n = int(input())
    di = {}
    for _ in range(n):
        user_input = input().split(':')
        value = user_input[0].strip(' {}":\'')
        key = user_input[1].strip(' {}":\'')
        di[key] = value
    has_garfield = "Cat01" in di or "Garfield" in di.values()
    has_fubuki = "Fox01" in di or "Fubuki" in di.values()
    if not has_garfield:
        di["Cat01"] = "Garfield"
    if not has_fubuki:
        di["Fox01"] = "Fubuki"
    cat_count = sum(1 for k in di if k.startswith("Cat"))
    fox_count = sum(1 for k in di if k.startswith("Fox"))
    print(f"Cat : {cat_count}")
    print(f"Fox : {fox_count}")
    sorted_items = sorted(di.items(), key=lambda item: (item[0][:3], int(item[0][3:])))
    for key, value in sorted_items:
        print(f"{value} : {key}")
main()
