class Student:
    def __init__(self, name, email, grades):
        self.name = name # string
        self.email = email # string
        self.grades = grades # List of integers

    def add_grade(self, grade):
        """Adds a grade to the grades list."""
        self.grades.append(grade)

    def average_grade(self):
        """Returns the average of all grades."""
        if not self.grades:
            return 0
        return sum(self.grades) / len(self.grades)

    def display_info(self):
        """Prints the student’s name, email, and grades."""
        print(f"Name: {self.name}, Email: {self.email}, Grades: {self.grades}")

    def grades_tuple(self):
        """Returns the grades as a tuple."""
        return tuple(self.grades)
    
# Create 3 student objects
student1 = Student("Alice", "alice@example.com", [85, 90, 78])
student2 = Student("Bob","bob@example.com", [88, 92, 79])
student3 = Student("Charlie", "charlie@example.com", [90, 85, 87])

student1.add_grade(95)
student2.add_grade(80)

student1.display_info()
student2.display_info()
student3.display_info()


