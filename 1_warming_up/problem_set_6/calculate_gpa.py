grade_points_dict = {
    "A": 16,
    "B": 14,
    "C": 12,
    "D": 10,
    "E": 8,
    "F": 6,
    "G": 2
}


def get_grade_point(grade):
    return grade_points_dict.get(grade, 0)


def print_student_details(student_details):
    for student in student_details:
        print(student)


def get_student_gpa_groups(students):
    gpa_atleast_ten = []
    gpa_less_than_ten = []

    for student_id, results in students.items():
        all_credits = results[0]
        gpa = float(results[1])

        if gpa >= 10.00:
            gpa_atleast_ten.append(f"ID: {student_id} Credits: {all_credits} GPA: {gpa}")
        elif gpa < 10.00:
            gpa_less_than_ten.append(f"ID: {student_id} Credits: {all_credits} GPA: {gpa}")

    return gpa_atleast_ten, gpa_less_than_ten


def calculate_gpa():
    students = {}

    with open("problem_set_6_students.txt") as student_file:
        for student_line in student_file:
            total_credits = 0
            total_grade_points = 0

            student_data = student_line.split()
            student_id = student_data.pop(0)

            student_results = [student_data[i:i + 3] for i in range(0, len(student_data), 3)]
            for result in student_results:
                student_credits = int(result[1])
                grade = get_grade_point(result[2])
                student_grade_points = student_credits * grade

                total_credits += student_credits
                total_grade_points += student_grade_points

            student_gpa = f"{float(total_grade_points / total_credits):.2f}"
            students[student_id] = (total_credits, student_gpa)

    gpa_atleast_ten, gpa_less_than_ten = get_student_gpa_groups(students)
    print("Students With GPA Atleast 10: ")
    print_student_details(gpa_atleast_ten)
    print("\nStudents With GPA Less Than 10: ")
    print_student_details(gpa_less_than_ten)


if __name__ == "__main__":
    calculate_gpa()
