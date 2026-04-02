from student_management import *

def display_menu():
    print("\n--- Student Management Menu ---")
    print("1. Add Student")
    print("2. View Student")
    print("0. Exit")
def main():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "0":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == "__main__":
    main()