"""
Week 2: Making Decisions & Repeating Tasks in Python
Project: Student Grade Calculator (grade_calculator.py)
"""


def calculate_grade(marks):
    """Evaluate marks (0-100) using if-elif-else and return (grade, message)."""
    if marks >= 90:
        return "A", "Outstanding! Excellent performance—keep shining! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good job! With a little more practice, you can reach the top! 📈"
    elif marks >= 60:
        return "D", "Fair effort! Review the key concepts and keep pushing forward! 💪"
    else:
        return "F", "Don't give up! Every mistake is a learning opportunity—you've got this next time! 🌱"


def get_student_name():
    """Prompt for student name using a while loop until a non-empty name is given."""
    while True:
        name = input("Enter student name: ").strip()
        if name:
            return name
        print("❌ Student name cannot be empty. Please enter a valid name.")


def get_valid_marks():
    """Use a while loop and try-except to validate marks within 0-100."""
    while True:
        raw_input = input("Enter marks (0-100): ").strip()
        try:
            marks = float(raw_input)
            if 0 <= marks <= 100:
                return int(marks) if marks.is_integer() else marks
            else:
                print("❌ Invalid input! Marks must be between 0 and 100. Please try again.")
        except ValueError:
            print("❌ Invalid input! Please enter a valid number between 0 and 100.")


def display_result(name, marks, grade, message):
    """Display the formatted grade report."""
    print(f"\n📊 RESULT FOR {name.upper()}:")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


def main():
    name = get_student_name()
    marks = get_valid_marks()
    grade, message = calculate_grade(marks)
    display_result(name, marks, grade, message)


if __name__ == "__main__":
    main()
