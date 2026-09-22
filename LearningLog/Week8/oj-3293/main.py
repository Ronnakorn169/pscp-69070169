"""BigFrame"""
def head_border(long):
    """print head border"""
    print("*"*long)
def print_order_text(all_text,longest_text_count):
    """order_text"""
    for i in all_text:
        shift = longest_text_count-len(i)
        print("* "+i+(" "*shift)+" *")
def main():
    """Main function"""
    text1 = ""
    text2 = ""
    text3 = ""
    text4 = ""
    text5 = ""
    try:
        text1 = input().strip()
        text2 = input().strip()
        text3 = input().strip()
        text4 = input().strip()
        text5 = input().strip()
    except EOFError:
        pass
    order_text = [text1,text2,text3,text4,text5]
    longest_text_count = max(
        len(text1),len(text2),len(text3)
        ,len(text4),len(text5),
    )
    head_border(longest_text_count+4)
    print_order_text(order_text,longest_text_count)
    head_border(longest_text_count+4)
main()
