"""docstring module"""
def main():
    """main function"""
    text = input()
    order = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for ch in order:
        count = text.count(ch)
        if count > 0:
            chunks = []
            while count > 5:
                chunks.append("-----")
                count -= 5
            chunks.append("-" * count)
            print(f"{ch} : {'|'.join(chunks)}")
main()
