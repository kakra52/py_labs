class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 12:
            self.grades.append(grade)
        else:
            print(f"Помилка: оцінка {grade} не додається.")

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name}: {self.grades}, середній = {self.average():.2f}"


student = Student("Ivan Petrenko")

student.add_grade(10)
student.add_grade(12)
student.add_grade(15)
student.add_grade(9)

print(student)
