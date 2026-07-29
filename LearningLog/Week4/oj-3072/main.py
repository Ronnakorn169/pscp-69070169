"""docstring module"""
def main():
    """main function"""
    text = input().lower()
    alphabet = []
    for i in text:
        if i in ["a","e","i","o","u"]:
            alphabet.append(i)
    unique_alphabet = list(dict.fromkeys(alphabet))
    unique_alphabet.sort()
    for i in unique_alphabet:
        print(f"{i} : {alphabet.count(i)}")
main()
