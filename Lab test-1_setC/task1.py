#Develop a python program for SRU_Student class with the properties like Name , Roll NO and Department , make a Student_Data which stores as txt
class SRU_Student:
    def __init__(self, name, roll_no, department):
        self.name = name
        self.roll_no = roll_no
        self.department = department

    def __str__(self):
        return f"Name: {self.name}, Roll No: {self.roll_no}, Department: {self.department}"

def save_student_data(student, filename="Student_Data.txt"):
    with open(filename, "a") as file:
        file.write(str(student) + "\n")

# Example usage
if __name__ == "__main__":
    name = input("Enter student name: ")
    roll_no = input("Enter roll number: ")
    department = input("Enter department: ")

    student = SRU_Student(name, roll_no, department)
    save_student_data(student)
    print("Student data saved to Student_Data.txt")