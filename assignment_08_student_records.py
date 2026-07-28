# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
# =============================================================================


def add_student(students):
    """Feature 1: Collects name, ID, and scores, then adds the record."""
    name = input("Student name: ")
    student_id = int(input("Student ID: "))

    num_scores = int(input("How many scores? "))
    scores = []
    for i in range(num_scores):
        score = float(input(f"Enter score {i + 1}: "))
        scores.append(score)

    student = {
        "name": name,
        "id": student_id,
        "scores": scores,
    }
    students.append(student)

    print(f'Student "{name}" added successfully.')


def calculate_average(scores):
    """Helper: Returns the average of a list of scores, rounded to 2 decimals."""
    if not scores:
        return 0.0
    return round(sum(scores) / len(scores), 2)


def display_all_students(students):
    """Feature 2: Prints a formatted table of every student's info."""
    if not students:
        print("No students have been added yet.")
        return

    print("-" * 60)
    print(f'{"Name":<15}{"ID":<12}{"Scores":<20}{"Average":<10}')
    print("-" * 60)

    for student in students:
        scores_str = ", ".join(str(s) for s in student["scores"])
        average = calculate_average(student["scores"])
        print(f'{student["name"]:<15}{student["id"]:<12}{scores_str:<20}{average:<10}')

    print("-" * 60)


def find_student_average(students, student_id):
    """Feature 3: Finds a student by ID and returns their average score.

    Returns None if no student with that ID exists.
    """
    for student in students:
        if student["id"] == student_id:
            return calculate_average(student["scores"])
    return None


def run_add_student(students):
    add_student(students)


def run_display_all(students):
    display_all_students(students)


def run_calculate_average(students):
    student_id = int(input("Enter student ID: "))
    average = find_student_average(students, student_id)

    if average is None:
        print(f"Error: No student found with ID {student_id}.")
        return

    # find the student's name for the confirmation message
    for student in students:
        if student["id"] == student_id:
            print(f"{student['name']}'s average score: {average}")
            break


def print_menu():
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == "1":
            run_add_student(students)
        elif choice == "2":
            run_display_all(students)
        elif choice == "3":
            run_calculate_average(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")


if __name__ == "__main__":
    main()
