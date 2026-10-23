"""docstring module"""
def main():
    """main function"""
    data = {}
    while True:
        student_id = input()
        if student_id == "END":
            break
        year = student_id[:2]
        faculty = int(student_id[2:4])
        if year not in data:
            data[year] = {}
        data[year][faculty] = data[year].get(faculty, 0) + 1
    for year in sorted(data):
        first = True
        for faculty in sorted(data[year]):
            if first:
                print(f"{year} {faculty} {data[year][faculty]}")
                first = False
            else:
                print(f"-- {faculty} {data[year][faculty]}")
main()
