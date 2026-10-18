
try:
    a = float(input("A: "))
    b = float(input("B: "))
    op = input("Операція: + - * / ")

    if op == "+":
        print("Результат:", a + b)
    elif op == "-":
        print("Результат:", a - b)
    elif op == "*":
        print("Результат:", a * b)
    elif op == "/":
        print("Результат:", a / b)
    else:
        print("Помилка: невідома операція.")

except ValueError:
    print("Помилка: потрібно ввести числа.")
except ZeroDivisionError:
    print("Помилка: на нуль ділити не можна.")
