class Person:
    def __init__(self, name):
        self.name = name

class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

    def info(self):
        return f"Учень: {self.name}, група: {self.group}"

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def info(self):
        return f"Викладач: {self.name}, предмет: {self.subject}"

class Course:
    def __init__(self, title, teacher):
        self.title = title
        self.teacher = teacher
        self.students = []

    def add_student(self, student):
        for s in self.students:
            if s.name.lower() == student.name.lower():
                print(f"Студент з ПІБ {student.name} вже є на курсі.")
                return False
        self.students.append(student)
        return True

    def remove_student(self, name):
        for s in self.students:
            if s.name.lower() == name.lower():
                self.students.remove(s)
                return True
        return False

    def show_students(self):
        print(f"Курс: {self.title}")
        print(self.teacher.info())
        print("Студенти:")
        for idx, s in enumerate(self.students, 1):
            print(f"{idx}. {s.info()}")

teacher = Teacher("Olena Kovalenko", "Python")
course = Course("Python", teacher)

s1 = Student("Anna Ivanenko", "IT-10")
s2 = Student("Olha Petrova", "IT-10")
s3 = Student("Ivan Sydorov", "IT-11")
s4 = Student("Dmytro Koval", "IT-12")

course.add_student(s1)
course.add_student(s2)
course.add_student(s3)
course.add_student(s4)

course.add_student(Student("Anna Ivanenko", "IT-10"))

course.show_students()

course.remove_student("Ivan Sydorov")

print("\nПісля видалення:")
course.show_students()
