"""docstring"""
import json
def main():
    """main function"""
    dict_student = json.loads(input())
    thredholds = float(input())
    new_dict = sorted(dict(filter(lambda i: i[1] >= thredholds,dict_student.items()))\
                      .items(),key=lambda x:x[0])
    if new_dict:
        for i,v in new_dict:
            print(f"{i}\t{v:.2f}")
        return
    print("Nope")
main()
