# ==========================================
# Project: Student Management System
# Level: Python Fundamentals (University Year 1)
# Description: A simple program to manage student grades and save them to a file.
# ==========================================

import os

# File to save data
FILE_NAME = "student_data.txt"
students = []

def load_data():
    """Loads students from the text file into the list."""
    # Check if file exists first
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                for line in file:
                    # Data format in file: ID,Name,Grade
                    parts = line.strip().split(",")
                    if len(parts) == 3:
                        student = {
                            "id": parts[0], 
                            "name": parts[1], 
                            "grade": parts[2]
                        }
                        students.append(student)
            print(f"[System] Loaded {len(students)} students from file.\n")
        except Exception as e:
            print("[Error] Could not load data.\n")
    else:
        print("[System] No data file found. Starting new list.\n")

def save_data():
    """Saves the current student list to the text file."""
    try:
        with open(FILE_NAME, "w") as file:
            for s in students:
                # Saving as: ID,Name,Grade
                line = f"{s['id']},{s['name']},{s['grade']}\n"
                file.write(line)
        print("[System] Data saved successfully!")
    except Exception as e:
        print("[Error] Could not save data.\n")

def add_student():
    """Adds a new student to the list."""
    print("--- Add New Student ---")
    s_id = input("Enter Student ID: ")
    
    # Simple validation: Check if ID already exists
    for s in students:
        if s['id'] == s_id:
            print("[Error] This ID already exists! Try again.\n")
            return

    name = input("Enter Student Name: ")
    grade = input("Enter Student Grade: ")

    # Create dictionary
    new_student = {"id": s_id, "name": name, "grade": grade}
    students.append(new_student)
    
    # Auto-save after adding
    save_data()
    print(f"[Success] Student {name} added.\n")

def view_students():
    """Prints all students in a readable format."""
    print("--- Student List ---")
    if len(students) == 0:
        print("No students found.")
    else:
        print(f"{'ID':<10} {'Name':<20} {'Grade':<10}")
        print("-" * 40)
        for s in students:
            print(f"{s['id']:<10} {s['name']:<20} {s['grade']:<10}")
    print("-" * 40 + "\n")

def delete_student():
    """Deletes a student by ID."""
    print("--- Delete Student ---")
    s_id = input("Enter ID to delete: ")
    
    found = False
    for i in range(len(students)):
        if students[i]['id'] == s_id:
            removed = students.pop(i)
            found = True
            print(f"[Success] Student {removed['name']} deleted.")
            save_data() # Auto-save after deleting
            break
            
    if not found:
        print("[Error] Student ID not found.\n")

def menu():
    """Main program loop."""
    # Load data when program starts
    load_data()
    
    while True:
        print("=== STUDENT SYSTEM MENU ===")
        print("1. Add Student")
        print("2. View Students")
        print("3. Delete Student")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        print() # Empty line for look

        if choice == '1':
            add_student()
        elif choice == '2':
            view_students()
        elif choice == '3':
            delete_student()
        elif choice == '4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.\n")

# Start the program
if __name__ == "__main__":
    menu()