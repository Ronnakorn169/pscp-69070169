"""docstring module"""
def trash_collector():
    """core function"""
    errorList = []
    plastic , can , glass = map(float,input().split(" "))
    total = plastic + can + glass
    errorList.append(str(f"{total:.1f}"))
    if total > 50:
        errorList.append("Overloaded")
    if plastic > 20:
        errorList.append("Check Type Plastic")
    if can > 20:
        errorList.append("Check Type Can")
    if glass > 20:
        errorList.append("Check Type Glass")
    print(", ".join(errorList))
def main():
    """main function"""
    n = int(input())
    for _ in range(n):
        trash_collector()
main()
