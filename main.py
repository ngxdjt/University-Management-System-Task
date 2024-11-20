from random import randint

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_details(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def get_details(self):
        return f"Name: {self.name}, Age: {self.age}, Gender: {self.gender}"

class Student(Person):
    def __init__(self, name, age, gender, student_id, course):
        super().__init__(name, age, gender)
        self.id = student_id
        self.course = course
        self.grades = []

    def set_student_details(self, student_id, course):
        self.id = student_id
        self.course = course

    def add_grade(self, grade):
        self.grades.append(grade)

    def calculate_average_grade(self):
        if not self.grades:
            return 0
        else:
            return sum(self.grades)/len(self.grades)
        
    def get_student_summary(self):
        return f"{self.get_details()} Student ID: {self.id} Course: {self.course} Average Grade: {self.calculate_average_grade()}"
    
class Professor(Person):
    def __init__(self, name, age, gender, staff_id, department, salary):
        super().__init__(name, age, gender)
        self.id = staff_id
        self.department = department
        self.salary = salary

    def set_professor_details(self, staff_id, department, salary):
        self.id = staff_id
        self.department = department
        self.salary = salary

    def give_feedback(self, student: Student, feedback: str):
        print(f"Feedback for {student.name}: {feedback}")

    def get_professor_summary(self):
        return f"{self.get_details()} Staff ID: {self.id} Department: {self.department} Salary: {self.salary}"
    
class Administrator(Person):
    def __init__(self, name, age, gender, admin_id, office, years_of_service):
        super().__init__(name, age, gender)
        self.id = admin_id
        self.office = office
        self.years = years_of_service

    def set_admin_details(self, admin_id, office, years_of_service):
        self.id = admin_id
        self.office = office
        self.years = years_of_service

    def increment_service_years(self):
        self.years += 1

    def get_admin_summary(self):
        return f"{self.get_details()} Admin ID: {self.id} Office: {self.office} Years of Service: {self.years}"
    

student1 = Student("Bob", 18, "Male", "S2352", "Maths")
student2 = Student("Dave", 19, "Male", "S2312", "Physics")

prof1 = Professor("Eve", 35, "Female", "P7531", "Maths", 30000)
prof2 = Professor("Paul", 64, "Male", "P6261", "Physics", 32000)

admin = Administrator("Callum", 48, "Male", "A9801", "U34", 10)


print(student1.get_student_summary())
print(prof1.get_professor_summary())
print(admin.get_admin_summary())

for i in range(5):
    student1.add_grade(randint(1,9))
averageGrade = student1.calculate_average_grade()

prof1.give_feedback(student1, "Well done on your work")
prof1.salary *= 1.1

admin.increment_service_years()

print(student1.get_student_summary())
print(prof1.get_professor_summary())
print(admin.get_admin_summary())