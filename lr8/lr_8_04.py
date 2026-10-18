
students = []
skipped = 0

try:
    with open("students.txt", "r", encoding="utf-8") as file:
        for number, line in enumerate(file, 1):
            try:
                parts = line.strip().split(";")

                if len(parts) != 2:
                    raise ValueError("неправильний формат")

                name = parts[0].strip()

                if len(name.split()) != 2:
                    raise ValueError("неправильне ім'я")

                try:
                    grade = int(parts[1].strip())
                except ValueError:
                    raise ValueError("бал не є числом")

                if grade < 0 or grade > 100:
                    raise ValueError("бал поза діапазоном")

                students.append((name, grade))

            except ValueError as e:
                skipped += 1
                print(f"Рядок {number} пропущено: {e}.")

    students.sort(key=lambda x: x[1], reverse=True)

    with open("report.txt", "w", encoding="utf-8") as file:
        for name, grade in students:
            file.write(f"{name};{grade}\n")

    print("Правильних записів:", len(students))
    print("Пропущено:", skipped)
    print("Створено report.txt")

except FileNotFoundError:
    print("Помилка: файл students.txt не знайден.")
