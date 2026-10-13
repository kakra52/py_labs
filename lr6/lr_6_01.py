import math

r = float(input("Радіус: "))
a = float(input("Перший катет: "))
b = float(input("Другий катет: "))
n = int(input("Предметів: "))
k = int(input("В упаковці: "))

if r < 0 or a < 0 or b < 0 or n < 0 or k <= 0:
    print("Помилка введення!")
else:
    area = math.pi * r ** 2
    hypotenuse = math.sqrt(a ** 2 + b ** 2)
    packages = math.ceil(n / k)

    print("Площа круга:", round(area, 2))
    print("Гіпотенуза:", round(hypotenuse, 2))
    print("Потрібно упаковок:", packages)