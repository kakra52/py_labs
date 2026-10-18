
students = ["Іван", "Оля", "Петро", "Марія"]
grades = {
    "Математика": 11,
    "Фізика": 10,
    "Інформатика": 12
}

choice = input("1 - учень, 2 - предмет: ")

if choice == "1":
    try:
        index = int(input("Індекс: "))
        if index < 0:
            raise IndexError
        print("Учень:", students[index])
    except ValueError:
        print("Помилка: індекс повинен бути числом.")
    except IndexError:
        print("Помилка: учня з таким індексом немає.")

elif choice == "2":
    subject = input("Предмет: ")
    try:
        print("Оцінка:", grades[subject])
    except KeyError:
        print("Помилка: такого предмета немає.")

else:
    print("Помилка: невідомий пункт меню.")
