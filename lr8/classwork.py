# if 7 >5 :
#     print("ok")


# n = int("number")
# print(n)

# try:
#     age = int(input("age:"))
#     print("your age is",age)
# except ValueError:
#     print("please enter valid age")
#value error коли тип операцыъ правильний але тип операції не можливий з даним формат

# try:
#     a = int(input("a"))
#     b = int(input("b"))
#     result = a / b
#     print(result)
# except ValueError:
#     print("a b мають бути числами")
# except ZeroDivisionError:
#     print("ділити на 0 неможна")
# finally:
#     print("все скінчилось")
# while True:
#     try:
#         grade = int(input("enter your grade"))
#         if grade < 1 or grade > 12:
#             raise ValueError("Grade must be betwet 1 and 12")
#         print(f'Your grade is {grade}')
#         break
#     except ValueError as error_limit:
#         print(f'Error: {error_limit}')
# def int_input(message):
#     while True:
#         try:
#             return int(input(message))
#         except ValueError:
#             print("please enter integer")
# n = int_input("Please enter a number")
# print(n)

# def input_grade():
#     while True:
#         try:
#             grade = int(input("enter your grade 1...12"))
#             if grade < 1 or grade > 12:
#                 raise ValueError("Grade must be betwen 1 and 12")
#             return grade
#         except ValueError as error:
#             print(error)
#
# grade = input_grade()
# print(f"Оцінка {grade} прийнята")


# price = {
#     "apple":10,
#     "banana":20,
# }
# product = input("enter product name")
# try:
#     print(price[product])
# except KeyError:
#     print("Product not found")

# product = input("enter product name")
# price = price.get(product,"product not found")

# try:
#     with open('data.txt', "r",encoding="utf-8") as f:
#         data = f.read()
#         print(data)
# except FileNotFoundError:
#     print("file not found")

# line = 'Ivan;95'
# parts = line.strip().split(';')
# if len(parts) != 2:
#     print("error in line")
# else:
#     name = parts[0]
#     grade = parts[1]
#
#
#     try:
#         grade_int = int(grade)
#         if grade_int < 0 or grade_int > 100:
#             raise ValueError("Бaл не відповідає від 1 до 100 ")
#     except ValueError as e:
#         print(f'Помилка {e}')
#     else:
#         print(f"Правильний запис: {name} - {grade_int}")

# lines = [
#     "Ivan;95",
#     "liza;99",
#     "vadymka;100"
# ]
# for line_number, line in enumerate(lines,start=1):
#     parts = line.strip().split(";")
#     if len(parts) != 2:
#         print(f'рядок {line_number} має помилку')
#         continue
#     name = parts[0]
#     try:
#         score = int(parts[1])
#     except ValueError:
#         print(f'Рядок {line_number} пропущено, бал виставлений неправильно')
#         continue
#     print(f'Правильний запис {name} - {score}')
