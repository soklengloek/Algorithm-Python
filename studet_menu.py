def input_score(scores):
    """Input a student score for multiple subjects"""
    try:
        name = input("Enter student name: ")
        subjects = ["Math", "English", "Science", "History"]
        student_scores = {}
        
        for subject in subjects:
            score = float(input(f"Enter {subject} score (0-100): "))
            if 0 <= score <= 100:
                student_scores[subject] = score
            else:
                print(f"{subject} score must be between 0 and 100!")
                return
        
        scores[name] = student_scores
        print(f"Scores for {name} recorded successfully!\n")
    except ValueError:
        print("Invalid input. Please enter a valid number.\n")


def view_scores(scores):
    """View all recorded scores"""
    if not scores:
        print("No scores recorded yet.\n")
    else:
        print("\n--- Student Scores ---")
        for name, score in scores.items():
            print(f"{name}: {score}")
        print()


def calculate_stats(scores):
    """Calculate total, average, and grade"""
    if not scores:
        print("No scores to calculate.\n")
        return
    
    all_scores = []
    for student_scores in scores.values():
        all_scores.extend(student_scores.values())
    
    total = sum(all_scores)
    average = total / len(all_scores)
    
    if average >= 90:
        grade = "A"
    elif average >= 80:
        grade = "B"
    elif average >= 70:
        grade = "C"
    elif average >= 60:
        grade = "D"
    else:
        grade = "F"
    
    print(f"\n=== Student Score ====")
    print(f"Total: {total}")
    print(f"Average: {average:.2f}")
    print(f"Grade: {grade}\n")


def main():
    """Main menu"""
    scores = {}
    
    while True:
        print("--- Student Score Menu ---")
        print("1. Input Score")
        print("2. View Scores")
        print("3. Calculate Total, Average, Grade")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            input_score(scores)
        elif choice == "2":
            view_scores(scores)
        elif choice == "3":
            calculate_stats(scores)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()