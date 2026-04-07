class Student:
    def __init__(self, student_id, name, score):
        self.student_id = student_id
        self.name = name
        self.score = score
    
    def __repr__(self):
        return f"ID: {self.student_id}, Name: {self.name}, Score: {self.score}"
class StudentManagementSystem:
    def __init__(self):
        self.students = []  
    def add_student(self, student_id, name, score):
        """Add a new student"""
        student = Student(student_id, name, score)
        self.students.append(student)
        print(f"Student {name} added successfully!")   
    def show_students(self):
        """Display all students"""
        if not self.students:
            print("No students in the system.")
            return
        print("\n--- Student List ---")
        for student in self.students:
            print(student)
        print()  
    def average_score(self):
        """Calculate average score"""
        if not self.students:
            print("No students to calculate average.")
            return
        avg = sum(s.score for s in self.students) / len(self.students)
        print(f"Average Score: {avg:.2f}\n")   
    def highest_score(self):
        """Find student with highest score"""
        if not self.students:
            print("No students in the system.")
            return
        highest = max(self.students, key=lambda s: s.score)
        print(f"Highest Score: {highest}\n")   
    def delete_student(self, student_id):
        """Delete student by ID"""
        for student in self.students:
            if student.student_id == student_id:
                self.students.remove(student)
                print(f"Student {student.name} deleted successfully!\n")
                return
        print("Student not found!\n")    
    def update_student(self, student_id, name=None, score=None):
        """Update student information"""
        for student in self.students:
            if student.student_id == student_id:
                if name:
                    student.name = name
                if score is not None:
                    student.score = score
                print(f"Student updated: {student}\n")
                return
        print("Student not found!\n")
if __name__ == "__main__":
    system = StudentManagementSystem()
    while True:
        print("--- Student Management System ---")
        print("1. Add Student")
        print("2. Show Students")
        print("3. Average Score")
        print("4. Highest Score")
        print("5. Delete Student")
        print("6. Update Student")
        print("7. Exit")       
        choice = input("Enter your choice (1-7): ")       
        if choice == "1":
            sid = input("Enter Student ID: ")
            name = input("Enter Student Name: ")
            score = float(input("Enter Student Score: "))
            system.add_student(sid, name, score)        
        elif choice == "2":
            system.show_students()       
        elif choice == "3":
            system.average_score()       
        elif choice == "4":
            system.highest_score()       
        elif choice == "5":
            sid = input("Enter Student ID to delete: ")
            system.delete_student(sid)        
        elif choice == "6":
            sid = input("Enter Student ID to update: ")
            name = input("Enter new name (press Enter to skip): ") or None
            score_input = input("Enter new score (press Enter to skip): ")
            score = float(score_input) if score_input else None
            system.update_student(sid, name, score)       
        elif choice == "7":
            print("Exiting...")
            break        
        else:
            print("Invalid choice! Please try again.\n")