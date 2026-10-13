from datetime import date

try:
    year = int(input("Рік: "))
    month = int(input("Місяць: "))
    day = int(input("День: "))

    event = date(year, month, day)
    today = date.today()

    if event > today:
        days = (event - today).days
        print("До події залишилося:", days, "днів")

    elif event < today:
        days = (today - event).days
        print("Після події минуло:", days, "днів")

    else:
        print("Подія відбувається сьогодні!")

except ValueError:
    print("Помилка! Неправильна дата.")