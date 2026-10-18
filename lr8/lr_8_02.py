
def input_grade():
    while True:
        try:
            grade = int(input("Оцінка: "))

            if grade < 1 or grade > 12:
                raise ValueError("діапазон")

            return grade

        except ValueError as e:
            if str(e) == "діапазон":
                print("Помилка: оцінка повинна бути від 1 до 12.")
            else:
                print("Помилка: потрібно ввести ціле число.")

grade = input_grade()
print("Прийнято:", grade)
