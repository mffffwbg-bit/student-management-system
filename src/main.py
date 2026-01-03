# ==========================================
# Project: Student Management System (OOP Version)
# Features: CRUD, Search, File I/O, Class Structure
# ==========================================

import os

FILE_NAME = "student_data.txt"

# 1. CLASS: Tek bir öğrenciyi temsil eder
class Student:
    def __init__(self, student_id, name, grade):
        self.student_id = student_id
        self.name = name
        self.grade = grade

    def __str__(self):
        # Öğrenciyi yazdırdığımızda nasıl görüneceği
        return f"{self.student_id:<10} {self.name:<20} {self.grade:<10}"

    def to_file_format(self):
        # Dosyaya kaydederken kullanılacak format
        return f"{self.student_id},{self.name},{self.grade}\n"

# 2. MANAGER CLASS: Tüm listeyi ve işleri yönetir
class StudentManager:
    def __init__(self):
        self.students = []
        self.load_data()

    def load_data(self):
        if os.path.exists(FILE_NAME):
            try:
                with open(FILE_NAME, "r") as file:
                    self.students = []
                    for line in file:
                        parts = line.strip().split(",")
                        if len(parts) == 3:
                            # Dosyadan okuyup "Student" nesnesine çeviriyoruz
                            new_student = Student(parts[0], parts[1], parts[2])
                            self.students.append(new_student)
                print(f"[System] {len(self.students)} students loaded.")
            except Exception:
                print("[Error] Could not load data.")
        else:
            print("[System] No data file found. Starting fresh.")

    def save_data(self):
        try:
            with open(FILE_NAME, "w") as file:
                for student in self.students:
                    file.write(student.to_file_format())
            print("[System] Data saved successfully!")
        except Exception:
            print("[Error] Could not save data.")

    def add_student(self):
        print("\n--- Add New Student ---")
        s_id = input("ID: ")
        
        # ID Kontrolü (Aynı ID var mı?)
        if self.find_student_by_id(s_id):
            print("[Error] This ID already exists!")
            return

        name = input("Name: ")
        grade = input("Grade: ")
        
        # Yeni nesne oluştur ve listeye ekle
        new_student = Student(s_id, name, grade)
        self.students.append(new_student)
        self.save_data()
        print(f"[Success] {name} added.")

    def search_student(self):
        print("\n--- Search Student ---")
        keyword = input("Enter ID or Name to search: ").lower()
        
        found_students = []
        for s in self.students:
            # Hem isme hem ID'ye bakar
            if keyword in s.student_id.lower() or keyword in s.name.lower():
                found_students.append(s)

        if found_students:
            print(f"\n{'ID':<10} {'Name':<20} {'Grade':<10}")
            print("-" * 40)
            for s in found_students:
                print(s) # __str__ fonksiyonunu kullanır
        else:
            print("[Result] No matching students found.")

    def update_grade(self):
        print("\n--- Update Grade ---")
        s_id = input("Enter Student ID: ")
        
        student = self.find_student_by_id(s_id)
        if student:
            print(f"Current info: {student}")
            new_grade = input("Enter New Grade: ")
            student.grade = new_grade
            self.save_data()
            print("[Success] Grade updated.")
        else:
            print("[Error] Student not found.")

    def delete_student(self):
        print("\n--- Delete Student ---")
        s_id = input("Enter ID to delete: ")
        
        student = self.find_student_by_id(s_id)
        if student:
            self.students.remove(student)
            self.save_data()
            print("[Success] Student deleted.")
        else:
            print("[Error] Student not found.")

    def view_all(self):
        print("\n--- All Students ---")
        if not self.students:
            print("List is empty.")
        else:
            print(f"{'ID':<10} {'Name':<20} {'Grade':<10}")
            print("-" * 40)
            for s in self.students:
                print(s)

    # Yardımcı Fonksiyon (Kod tekrarını önlemek için)
    def find_student_by_id(self, s_id):
        for s in self.students:
            if s.student_id == s_id:
                return s
        return None

# 3. MAIN: Programın başladığı yer
def main():
    manager = StudentManager() # Manager sınıfını başlat

    while True:
        print("\n=== UNI STUDENT SYSTEM ===")
        print("1. Add Student")
        print("2. Search Student") # İstenen özellik
        print("3. Update Grade")   # İstenen özellik
        print("4. Delete Student")
        print("5. View All")
        print("6. Exit")
        
        choice = input("Choice: ")

        if choice == '1': manager.add_student()
        elif choice == '2': manager.search_student()
        elif choice == '3': manager.update_grade()
        elif choice == '4': manager.delete_student()
        elif choice == '5': manager.view_all()
        elif choice == '6': break
        else: print("Invalid choice.")

if __name__ == "__main__":
    main()