def extract_student_info(student_dict):
    student = student_dict.get('student', {})
    name = student.get('name', {})
    details = student.get('details', {})
    full_name = f"{name.get('first', '')} {name.get('last', '')}".strip()
    branch = details.get('branch', '')
    sgpa = details.get('sgpa', '')
    # Ask the user to enter details
    first = input("Enter student's first name: ")
    last = input("Enter student's last name: ")
    branch = input("Enter student's branch: ")
    sgpa = input("Enter student's SGPA: ")

    full_name = f"{first} {last}".strip()

    return {
        'Full Name': full_name,
        'Branch': branch,
        'SGPA': sgpa
    }

# Call the function to prompt for input
if __name__ == "__main__":
    student_dict = {}
    info = extract_student_info(student_dict)
    print(info)