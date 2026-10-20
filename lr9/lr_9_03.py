class Student:
    def __init__(self, name):
        self.name = name
        self.grades = []

    def add_grade(self, grade):
        if 1 <= grade <= 12:
            self.grades.append(grade)

    def average(self):
        if len(self.grades) == 0:
            return 0
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f"{self.name} — {self.average():.2f}"


students = [
    Student("Anna"),
    Student("Ivan"),
    Student("Olha"),
    Student("Petro"),
    Student("Maria")
]

students[0].add_grade(10)
students[0].add_grade(11)
students[0].add_grade(11)

students[1].add_grade(9)
students[1].add_grade(10)

students[2].add_grade(11)
students[2].add_grade(12)
students[2].add_grade(11)

students[3].add_grade(8)
students[3].add_grade(9)
students[3].add_grade(10)

students[4].add_grade(12)
students[4].add_grade(10)
students[4].add_grade(11)

print("Список учнів:")
for student in students:
    print(student)

best_average = max(student.average() for student in students)

print("\nНайкращий результат:")
for student in students:
    if student.average() == best_average:
        print(student)
