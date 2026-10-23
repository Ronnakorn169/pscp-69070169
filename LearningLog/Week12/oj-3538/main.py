"""docstring module"""
def main():
    """main function"""
    text = input()
    checked = ""
    unpaired = ""

    for ch in text:
        if ch not in checked:
            checked += ch
            if text.count(ch) % 2:
                unpaired += ch

    if not unpaired:
        print("fully paired")
    else:
        print(unpaired)

main()
