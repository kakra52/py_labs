import random
import statistics

n = int(input("Кількість оцінок: "))

if n <= 0:
    print("Помилка! Кількість повинна бути додатною.")
else:
    grades = []

    for i in range(n):
        grades.append(random.randint(1, 12))

    print("Оцінки:", grades)
    print("Min:", min(grades))
    print("Max:", max(grades))
    print("Середнє:", round(statistics.mean(grades), 2))
    print("Медіана:", statistics.median(grades))

    high = 0

    for grade in grades:
        if grade >= 10:
            high += 1

    print("Оцінок 10–12:", high)