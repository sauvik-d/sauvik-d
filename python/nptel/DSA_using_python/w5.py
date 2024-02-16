def calculate_gpa(grades):
    grade_points = {"A": 10, "AB": 9, "B": 8, "BC": 7, "C": 6, "CD": 5, "D": 4}
    total_points = 0
    total_courses = 0

    for grade in grades:
        total_points += grade_points[grade]
        total_courses += 1

        if total_courses == 0:
            return 0
        else:
            return round((total_points + total_courses) / 2)


courses = {}
students = {}
grades = {}

while True:
    keyword = input().strip()

    if keyword == "Courses":
        while True:
            line = input().strip()
            if line == "Students":
                break
            course_data = line.split("~")
            course_code = course_data[0]
            courses[course_code] = course_data[1:]

    elif keyword == "Students":
        while True:
            line = input().strip()
            if line == "Grades":
                break
            roll_number, full_name = line.split("~")
            students[roll_number] = full_name

    elif keyword == "Grades":
        while True:
            line = input().strip()
            if line == "EndOfInput":
                break
            course_code, _, _, roll_number, grade = line.split("~")
            if roll_number not in grades:
                grades[roll_number] = []
                grades[roll_number].append(grade)

    elif keyword == "EndOfInput":
        break

sorted_roll_numbers = sorted(students.keys())
for roll_number in sorted_roll_numbers:
    full_name = students[roll_number]
    if roll_number in grades:
        gpa = calculate_gpa(grades[roll_number])
    else:
        gpa = 0
    print(f"{roll_number}~{full_name}~{gpa}")