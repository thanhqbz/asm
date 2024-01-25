def calculate_gpa(grades):
    
    tt_credits = 0
    for grade, credits in grades.items():
        tt_credits += credits
        gpa = tt_credits / credits
    return gpa


def print_gpa(student_name, gpa):
    print(f"{student_name}'s GPA: {gpa:.2f}")

def write_to_file(student_name, gpa):
    with open("gpa_results.txt", "w") as file:
        file.write(f"{student_name}'s GPA: {gpa:.2f}")
    print(f"GPA caculated successfully. Result saved to 'gpa_result.txt'")
g

def get_user_input(): 

    while True:
      student_name = input("Enter your name: ")
      if student_name.isalpha():
        break
      else:
        print("Error, invalid name")


    try:
        num_courses = int(input("Enter the number of courses: "))
        grades = {}

        for _ in range(num_courses):
            course_name = input("Enter the course name: ")
            grade = float(input(f"Enter the grade for {course_name}: "))
            credits = float(input(f"Enter the credits for {course_name}: "))

            grades[course_name] = grade * credits

        return student_name, grades
    except ValueError:
        print("Invalid input. Please enter valid numeric values for grades and credits.")
        return None, None

def main():
    student_name, grades = get_user_input()

    if student_name is not None and grades is not None:
        gpa = calculate_gpa(grades)
        print_gpa(student_name, gpa)
        write_to_file(student_name, gpa)

if __name__ == "__main__":
    main()
