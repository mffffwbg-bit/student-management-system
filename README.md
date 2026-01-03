# Student Management System

A Python program to manage student information with persistent file storage.

## Features

- Add new students with validation (no duplicate IDs)
- View all students in a formatted table
- Delete students by ID
- Auto-save data to file after each operation
- Load data from file when program starts

## How to Run
```bash
python src/main.py
```

## Menu Options

1. **Add Student** - Enter ID, name, and grade
2. **View Students** - Display all students in table format
3. **Delete Student** - Remove a student by ID
4. **Exit** - Close the program

## Data Storage

- Student data is saved in `student_data.txt`
- Format: `ID,Name,Grade`
- Data persists between sessions

## Technologies Used

- Python 3.11
- File I/O (reading/writing text files)
- Data structures (lists, dictionaries)
- Input validation

## Example
```
=== STUDENT SYSTEM MENU ===
1. Add Student
2. View Students
3. Delete Student
4. Exit

Enter your choice (1-4): 1
--- Add New Student ---
Enter Student ID: 101
Enter Student Name: John Doe
Enter Student Grade: 95
[Success] Student John Doe added.
```

## Author

mffffwbg-bit

## License

MIT
```

