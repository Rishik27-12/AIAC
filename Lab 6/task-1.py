class Student:
    def __init__(self, name, roll_no, marks):
        self.name, self.roll_no, self.marks = name, roll_no, marks

    def display_details(self):
        print(f"Name: {self.name}")
        print(f"Roll No: {self.roll_no}")
        print(f"Marks: {self.marks}")

    def calculate_grade(self):
        try:
            marks = float(self.marks)
            if marks < 0 or marks > 100:
                print("Error: Marks should be between 0 and 100.")
                return
            
            if marks >= 90: grade = 'A'
            elif marks >= 75: grade = 'B'
            elif marks >= 60: grade = 'C'
            else: grade = 'Fail'
            print(f"Grade: {grade}")
        except (ValueError, TypeError):
            print("Error: Marks should be a valid number.")

def get_valid_marks():
    while True:
        try:
            marks = float(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            print("Error: Marks should be between 0 and 100.")
        except ValueError:
            print("Error: Please enter a valid number.")

def main():
    print("=== Student Grade Calculator ===")
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    marks = get_valid_marks()
    
    student = Student(name, roll_no, marks)
    print("\n=== Student Details ===")
    student.display_details()
    student.calculate_grade()

# Run the program
if __name__ == "__main__":
    main()
