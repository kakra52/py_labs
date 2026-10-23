# import os
#
#
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def info(self):
#         return f"Ім'я: {self.name}"
#
#
# class Student(Person):
#     def __init__(self, name, group):
#         super().__init__(name)
#         self.group = group
#         self.grades = []
#
#     def info(self):
#         grades_display = self.grades if self.grades else "немає"
#         return f"Учень: {self.name}, Група: {self.group}, Оцінки: {grades_display}"
#
#     def add_grade(self, grade):
#         if 1 <= grade <= 12:
#             self.grades.append(grade)
#             return True
#         return False
#
#     def average(self):
#         if not self.grades:
#             return 0.0
#         return sum(self.grades) / len(self.grades)
#
#
# class Teacher(Person):
#     def __init__(self, name, subject):
#         super().__init__(name)
#         self.subject = subject
#
#     def info(self):
#         return f"Викладач: {self.name}, Предмет: {self.subject}"
#
#
# class Course:
#     def __init__(self, title, teacher):
#         self.title = title
#         self.teacher = teacher
#         self.students = []
#
#     def add_student(self, student):
#         self.students.append(student)
#
#     def remove_student(self, name):
#         for student in self.students:
#             if student.name.lower() == name.lower():
#                 self.students.remove(student)
#                 return True
#         return False
#
#     def find_student(self, name):
#         for student in self.students:
#             if student.name.lower() == name.lower():
#                 return student
#         return None
#
#     def average_rating(self):
#         if not self.students:
#             return 0.0
#         total = sum(student.average() for student in self.students)
#         return total / len(self.students)
#
#     def show_students(self):
#         print(f"КУРС: {self.title}")
#         print(f"{self.teacher.info()}")
#
#         if not self.students:
#             print("На курсі немає жодного студента.")
#             return
#
#         for idx, student in enumerate(self.students, 1):
#             print(f"{idx}. {student.info()} | Сер. бал: {student.average():.1f}")
#         print(f"Загальний середній рейтинг курсу: {self.average_rating():.1f}")
#
#     def save_to_file(self, filename="students.txt"):
#         try:
#             with open(filename, "w", encoding="utf-8") as file:
#                 for student in self.students:
#                     grades_str = ",".join(str(g) for g in student.grades)
#                     file.write(f"{student.name};{student.group};{grades_str}\n")
#             print("Дані успішно збережено у файл.")
#         except Exception as e:
#             print(f"Помилка при збереженні файлу: {e}")
#
#     def load_from_file(self, filename="students.txt"):
#         if not os.path.exists(filename):
#             print("Файл бази даних не знайдено. Буде створено новий під час збереження.")
#             return
#
#         try:
#             with open(filename, "r", encoding="utf-8") as file:
#                 self.students.clear()
#                 for line in file:
#                     line = line.strip()
#                     if not line:
#                         continue
#                     name, group, grades_text = line.split(";")
#                     student = Student(name, group)
#                     if grades_text:
#                         for grade in grades_text.split(","):
#                             student.add_grade(int(grade))
#                     self.add_student(student)
#             print("Дані успешно завантажено з файлу.")
#         except Exception as e:
#             print(f"Помилка при читанні файлу або пошкоджено його формат: {e}")
#
#
# def main():
#     teacher = Teacher("Олена Романівна", "Програмування Python")
#     course = Course("Основи об'єктно-орієнтованого програмування", teacher)
#     course.load_from_file()
#
#     while True:
#         print("\n--- ГОЛОВНЕ МЕНЮ ІНФОРМАЦІЙНОЇ СИСТЕМИ ---")
#         print("1 - Додати нового студента")
#         print("2 - Показати список усіх студентів та статистику курсу")
#         print("3 - Знайти студента за ПІБ та виставити оцінку")
#         print("4 - Видалити студента з курсу")
#         print("5 - Зберегти поточний стан у файл")
#         print("0 - Вихід із програми")
#
#         choice = input("Ваш вибір: ").strip()
#
#         if choice == "1":
#             name = input("Введіть ПІБ студента: ").strip()
#             group = input("Введіть назву групи (наприклад, ІТ-10): ").strip()
#             if name and group:
#                 new_student = Student(name, group)
#                 course.add_student(new_student)
#                 print(f"Студент '{name}' успішно доданий до списку.")
#             else:
#                 print("Помилка: Ім'я та група не можуть бути порожніми!")
#
#         elif choice == "2":
#             course.show_students()
#
#         elif choice == "3":
#             name = input("Введіть ПІБ студента для пошуку: ").strip()
#             student = course.find_student(name)
#
#             if student:
#                 print(f"Знайдено: {student.info()}")
#                 try:
#                     grade_input = input("Введіть оцінку (від 1 до 12) або натисніть Enter для скасування: ").strip()
#                     if grade_input:
#                         grade = int(grade_input)
#                         if student.add_grade(grade):
#                             print(f"Оцінку {grade} успішно додано студенту {student.name}.")
#                         else:
#                             print("Некоректний бал! Оцінка має бути виключно в межах від 1 до 12.")
#                 except ValueError:
#                     print("Помилка введення: Оцінка повинна бути цілим числом!")
#             else:
#                 print("Студента з таким ПІБ на курсі не знайдено.")
#
#         elif choice == "4":
#             name = input("Введіть ПІБ студента, якого потрібно видалити: ").strip()
#             if course.remove_student(name):
#                 print(f"Студента '{name}' успішно видалено з курсу.")
#             else:
#                 print("Не вдалося видалити: студента не знайдено.")
#
#         elif choice == "5":
#             course.save_to_file()
#
#         elif choice == "0":
#             save_before_exit = input("Бажаєте зберегти поточні зміни перед виходом? (так/ні): ").strip().lower()
#             if save_before_exit in ['так', 'т', 'y', 'yes']:
#                 course.save_to_file()
#             print("Роботу програми завершено. Успіхів у навчанні!")
#             break
#
#         else:
#             print("Невідомий пункт меню! Пожалуйста, оберіть цифру від 0 до 5.")
#
#
# if __name__ == "__main__":
#     main()
