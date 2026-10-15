# import os
#
# if not os.path.exists('text.txt'):
#     with open('text.txt', 'w', encoding="utf-8") as file:
#         file.write("Python - популярна мова програмування.\n")
#         file.write("Python використовується для роботи з даними.\n")
#         file.write("Файли дозволяють зберігати інформацію\n")
#         file.write("Python вимагає практики.\n")
#         file.write("Сьогодні ми працюємо з текстовими файлами.\n")
#
# if not os.path.exists('numbers.txt'):
#     with open('numbers.txt', 'w', encoding="utf-8") as file:
#         file.write("12\n8\n25\n4\n16\n")
#
# if not os.path.exists('students.txt'):
#     with open('students.txt', 'w', encoding="utf-8") as file:
#         file.write("Ivanenko Anna;91\n")
#         file.write("Leshchenko Ivan;76\n")
#         file.write("Komarova Sophie;97\n")
#         file.write("Bondarenko Illya;84\n")
#
# if not os.path.exists('grades.csv'):
#     with open('grades.csv', 'w', encoding="utf-8") as file:
#         file.write("Anna;Python;11\n")
#         file.write("Anna;Math;10\n")
#         file.write("Ivan;Python;6\n")
#         file.write("Ivan;Math;5\n")
#         file.write("Sophie;Python;11\n")
#         file.write("Sophie;Math;12\n")
#         file.write("Illya;Python;9\n")
#         file.write("Illya;Math;8\n")
#
# # with close   ; open opening
# # with open('hello.txt',"a",encoding="utf-8") as file:
# #     file.write("hello world!\n")
# #     file.write("hello world!\n")
# #     file.write("hello world!\n")
# #     file.write("hello world!\n")
#
# #w- режим запису
# #r - файл має існувати тільки читає
# #a додає в кінець старий зміст залишається
# # x створення нового файлу якщо однаковий файл 2 рази помилка
# # with open("text.txt","r",encoding="utf-8") as f:
# #     text = file.read()
# # print(f'read() => \n{text} \nlen() => \n{len(text)}')
# # with open("text.txt","r",encoding="utf-8") as file:
# #     line1 = file.readline()
# #     other_line = file.readline()
# #     line2 = file.readline()
# #
# #     print(line1)
# #     print(other_line)
# #     print(line2)
#
# # with open("text.txt","r",encoding="utf-8") as file:
# #     other_line = file.readline()
# # for line in other_line:
# #     print(line)
# # with open("text.txt","r",encoding="utf-8") as file:
# #     for number,line in enumerate(file,start=1):
# #         clean_line = line.strip()
# #         print(f'{number}.clean_line')
# # line = "Komarov Ivan;2\n"
# # clean_line = line.strip()
# # name, grade = clean_line.split(';')
# # print(name)
# # print(grade)
#
# # students = []
# # botanics = []
# # with open('students.txt', 'r', encoding="utf-8") as file:
# #     for line in file:
# #         name, grade = line.split(';')
# #         students.append([name, grade])
# #         if int(grade) >= 90:
# #             botanics.append([name, grade])
# # print(students)
# # print(botanics)
# # with open('botanics.txt', 'w', encoding="utf-8") as file:
# #     for name, grade in botanics:
# #         file.write(name + ';' + grade + '\n')
#
# # grades = []
# # with open("grades.csv", "r", encoding="utf-8") as file:
# #     for line in file:
# #         name,subject , grade = line.split(';')
# #         grades.append(grade)
# #         print(f"Ім'я {name}: {subject}: {grade}")
# #     average = int(sum(grades))/int(len(grades))