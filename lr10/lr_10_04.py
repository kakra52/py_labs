import os


class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Ім'я: {self.name}"


class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group
        self.grades = []

    def info(self):
        return f"Учень: {self.name}, група: {self.group}"

    def add_grade(self, grade):
        if 1 <= grade <= 12:
            self.grades.append(grade)
            return True
        return False

    def average(self):
        if not self.grades:
            return 0.0
        return sum(self.grades) / len(self.grades)


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
                print("Студент з таким ПІБ вже існує.")
                return False
        self.students.append(student)
        return True

    def remove_student(self, name):
        for s in self.students:
            if s.name.lower() == name.lower():
                self.students.remove(s)
                return True
        return False

    def find_student(self, name):
        for s in self.students:
            if s.name.lower() == name.lower():
                return s
        return None

    def add_grade_to_student(self, name, grade):
        student = self.find_student(name)
        if student:
            if student.add_grade(grade):
                print(f"Оцінку {grade} додано.")
            else:
                print("Неправильна оцінка. Має бути від 1 до 12.")
        else:
            print("Студента не знайдено.")

    def show_course(self):
        print(f"Курс: {self.title}")
        print(self.teacher.info())
        print("Список студентів:")
        for s in self.students:
            print(f"- {s.info()}")

    def show_rating(self):
        print("Рейтинг:")
        sorted_students = sorted(self.students, key=lambda x: x.average(), reverse=True)
        for idx, s in enumerate(sorted_students, 1):
            print(f"{idx}. {s.name} — {s.average():.2f}")

    def save_to_file(self, filename="course_data.txt"):
        try:
            with open(filename, "w", encoding="utf-8") as file:
                for s in self.students:
                    grades_str = ",".join(str(g) for g in s.grades)
                    file.write(f"{s.name};{s.group};{grades_str}\n")
            print("Дані збережено.")
        except IOError as e:
            print(f"Помилка при збереженні файлу: {e}")

    def load_from_file(self, filename="course_data.txt"):
        if not os.path.exists(filename):
            return
        try:
            with open(filename, "r", encoding="utf-8") as file:
                self.students.clear()
                for line in file:
                    line = line.strip()
                    if not line:
                        continue
                    parts = line.split(";")
                    if len(parts) == 3:
                        name, group, grades_str = parts
                        student = Student(name, group)
                        if grades_str:
                            for g in grades_str.split(","):
                                student.add_grade(int(g))
                        self.students.append(student)
            print("Дані відновлені з файлу.")
        except (ValueError, IOError) as e:
            print(f"Помилка при читанні або форматі файлу: {e}")


def main():
    teacher = Teacher("Olena Kovalenko", "Python")
    course = Course("Python", teacher)
    course.load_from_file()

    while True:
        print("\n1 — показати курс")
        print("2 — додати студента")
        print("3 — видалити студента")
        print("4 — знайти студента")
        print("5 — виставити оцінку")
        print("6 — показати рейтинг")
        print("7 — зберегти дані")
        print("0 — вихід")

        choice = input("Ваш вибір: ").strip()

        if choice == "1":
            course.show_course()
        elif choice == "2":
            name = input("ПІБ студента: ").strip()
            group = input("Група студента: ").strip()
            if name and group:
                course.add_student(Student(name, group))
            else:
                print("Ім'я та група не можуть бути порожніми.")
        elif choice == "3":
            name = input("ПІБ студента для видалення: ").strip()
            if course.remove_student(name):
                print("Студента видалено.")
            else:
                print("Студента не знайдено.")
        elif choice == "4":
            name = input("ПІБ для пошуку: ").strip()
            student = course.find_student(name)
            if student:
                print(student.info())
            else:
                print("Студента не знайдено.")
        elif choice == "5":
            name = input("ПІБ студента: ").strip()
            try:
                grade = int(input("Оцінка (1-12): ").strip())
                course.add_grade_to_student(name, grade)
            except ValueError:
                print("Оцінка має бути цілим числом.")
        elif choice == "6":
            course.show_rating()
        elif choice == "7":
            course.save_to_file()
        elif choice == "0":
            break
        else:
            print("Неправильний пункт меню.")


if __name__ == "__main__":
    main()
