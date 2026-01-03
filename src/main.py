# Student Management System
# Simple program to manage student information

students = []

def add_student():
    """Add a new student"""
    name = input("Enter student name: ")
    student_id = input("Enter student ID: ")
    grade = input("Enter grade: ")
    
    student = {
        "name": name,
        "id": student_id,
        "grade": grade
    }
    students.append(student)
    print(f"Student {name} added!\n")

def view_students():
    """Display all students"""
    if len(students) == 0:
        print("No students found!\n")
        return
    
    for i in range(len(students)):
        s = students[i]
        print(f"Name: {s['name']}, ID: {s['id']}, Grade: {s['grade']}")
    print()

def menu():
    """Main menu"""
    while True:
        print("--- Student Management ---")
        print("1. Add Student")
        print("2. View Students")
        print("3. Exit")
        
        choice = input("Choose (1-3): ")
        
        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!\n")

menu()