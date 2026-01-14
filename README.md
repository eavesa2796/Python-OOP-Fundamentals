# Student Class Example (Python)

## Overview
This project demonstrates a simple Python `Student` class used to store and manage student information, including names, email addresses, and grades. The class provides methods to add grades, calculate averages, display student details, and return grades in different formats.

## Features
- Store student name, email, and grades
- Add new grades dynamically
- Calculate the average grade
- Display student information in a readable format
- Convert grades from a list to a tuple

## Code Structure

### Student Class
The `Student` class includes:
- **Attributes**
  - `name` (string): Student’s name
  - `email` (string): Student’s email address
  - `grades` (list): A list of integer grades

- **Methods**
  - `add_grade(grade)`: Adds a new grade to the student’s grade list
  - `average_grade()`: Returns the average of all grades (returns 0 if no grades exist)
  - `display_info()`: Prints the student’s name, email, and grades
  - `grades_tuple()`: Returns the grades as a tuple

### Example Usage
The script creates three student objects, adds additional grades to two of them, and displays their information.

```python
student1 = Student("Alice", "alice@example.com", [85, 90, 78])
student2 = Student("Bob","bob@example.com", [88, 92, 79])
student3 = Student("Charlie", "charlie@example.com", [90, 85, 87])

student1.add_grade(95)
student2.add_grade(80)

student1.display_info()
student2.display_info()
student3.display_info()
