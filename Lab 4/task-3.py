# INSERT_YOUR_CODE
def extract_student_info(student_dict):
    student = student_dict.get('student', {})
    name = student.get('name', {})
    details = student.get('details', {})
    full_name = f"{name.get('first', '')} {name.get('last', '')}".strip()
    branch = details.get('branch', '')
    sgpa = details.get('sgpa', '')
    return {
        'Full Name': full_name,
        'Branch': branch,
        'SGPA': sgpa
    }

if __name__ == "__main__":
    first = input("Enter student's first name: ")
    last = input("Enter student's last name: ")
    branch = input("Enter student's branch: ")
    while True:
        try:
            sgpa = float(input("Enter student's SGPA: "))
            break
        except ValueError:
            print("Invalid SGPA. Please enter a numeric value.")
    student_dict = {
        'student': {
            'name': {'first': first, 'last': last},
            'details': {'branch': branch, 'sgpa': sgpa}
        }
    }
    info = extract_student_info(student_dict)
    print(info)

