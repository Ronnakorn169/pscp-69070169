"""docstring module"""
def main():
    """main function"""
    text = input().lower()
    count = 0
    for i in text:
        if i in ["a","e","i","o","u"]:
            count += 1
    print(count)
main()
