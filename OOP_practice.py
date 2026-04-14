import re


class Student:
	"""Represents a student and the grades they have earned."""

	def __init__(self, name, email, grades):
		self.name = name
		self.email = email
		self.grades = grades

	def add_grade(self, grade):
		"""Add one new grade to the student's grade list."""
		self.grades.append(grade)

	def average_grade(self):
		"""Return the average of all grades, or 0 when no grades exist."""
		if not self.grades:
			return 0
		return sum(self.grades) / len(self.grades)

	def display_info(self):
		"""Print the student's basic information."""
		print(f"Name: {self.name}")
		print(f"Email: {self.email}")
		print(f"Grades: {self.grades}")

	def grades_tuple(self):
		"""Return the student's grades as an immutable tuple."""
		return tuple(self.grades)


student_dict = {}


def get_student_by_email(email):
	"""Safely return a student object from the dictionary using the email key."""
	return student_dict.get(email)


def is_valid_email(email):
	"""Validate a simple name@domain.com email format using regex."""
	pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.com$"
	return bool(re.match(pattern, email))


def count_grades_above_90(students):
	"""Count how many grades are greater than 90 across all students."""
	return sum(1 for student in students for grade in student.grades if grade > 90)


def main():
	# Create three student objects with different starting grades.
	student1 = Student("Alice", "alice@example.com", [85, 90, 78])
	student2 = Student("Bob", "bob@example.com", [88, 92, 79])
	student3 = Student("Charlie", "charlie@example.com", [90, 85, 87])

	students = [student1, student2, student3]

	# Add two new grades to each student.
	student1.add_grade(95)
	student1.add_grade(88)
	student2.add_grade(80)
	student2.add_grade(94)
	student3.add_grade(91)
	student3.add_grade(89)

	print("Student Information and Averages")
	for student in students:
		student.display_info()
		print(f"Average Grade: {student.average_grade():.2f}")
		print(f"Email Valid: {is_valid_email(student.email)}")
		print("-" * 30)

	# Map each email to the matching student object.
	student_dict.clear()
	student_dict.update({student.email: student for student in students})

	print("Lookup by Email")
	found_student = get_student_by_email("alice@example.com")
	if found_student:
		found_student.display_info()
	else:
		print("Student not found.")
	print("-" * 30)

	# Build a set so repeated grades only appear once.
	unique_grades = {grade for student in students for grade in student.grades}
	print(f"Unique Grades: {unique_grades}")
	print("-" * 30)

	# Tuples cannot be modified, so this raises a TypeError.
	print("Tuple Immutability Demo")
	grades_as_tuple = student1.grades_tuple()
	print(f"Grades Tuple: {grades_as_tuple}")
	try:
		grades_as_tuple[0] = 100
	except TypeError as error:
		print(f"Tuples are immutable: {error}")
	print("-" * 30)

	print("List Operations")
	for student in students:
		removed_grade = student.grades.pop()
		print(f"Removed last grade for {student.name}: {removed_grade}")
		print(f"First Grade: {student.grades[0]}")
		print(f"Last Grade: {student.grades[-1]}")
		print(f"Number of Grades: {len(student.grades)}")
		print("-" * 30)

	print(f"Grades Above 90: {count_grades_above_90(students)}")


if __name__ == "__main__":
	main()
