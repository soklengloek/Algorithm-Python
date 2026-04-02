students = []

def add_student():
    name = input("Enter student name: ")
    student_id = int(input("Enter student ID: "))
    course = input("Enter course: ")
    students.append({"name": name, "id": student_id, "course": course})
    print("Student added successfully!\n")
def view_students():
    if not students:
        print("No students found.\n")
        return
    for student in students:
        print(f"ID: {student['id']}, Name: {student['name']}, Course: {student['course']}")
    print()
