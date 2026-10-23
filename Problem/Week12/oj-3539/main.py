"""docstring module"""
phones = {
    "iPhone 13 mini" : {
        "128 GB" : 25900,
        "256 GB" : 29900,
        "512 GB" : 37900
    },
    "iPhone 13" : {
        "128 GB" : 29900,
        "256 GB" : 33900,
        "512 GB" : 41900
    },
    "iPhone 13 Pro" : {
        "128 GB" : 38900,
        "256 GB" : 42900,
        "512 GB" : 50900,
        "1 TB" : 58900
    },
    "iPhone 13 Pro Max" : {
        "128 GB" : 42900,
        "256 GB" : 46900,
        "512 GB" : 54900,
        "1 TB" : 62900
    },
}
def main():
    """main"""
    model = input()
    capacity = input()
    try:
        print(phones.get(model,"Not Available").get(capacity,"Not Available"))
    except AttributeError:
        print("Not Available")
main()
