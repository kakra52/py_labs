import tkinter as tk
from tkinter import messagebox
import lr_6_04_1

students = ["Anna", "Ivan", "Olha"]


def create_report():
    value = entry.get().strip()

    if not value.isdecimal():
        messagebox.showerror("Помилка", "Введіть число від 1 до 20!")
        return

    count = int(value)

    if count < 1 or count > 20:
        messagebox.showerror("Помилка", "Введіть число від 1 до 20!")
        return

    report = ""

    for student in students:
        grades = lr_6_04_1.generate_grades(count)
        average = lr_6_04_1.average_grade(grades)
        level = lr_6_04_1.get_level(average)

        report += f"{student}: {grades} → {average:.2f} → {level}\n"

    print(report)

    text_result.delete("1.0", tk.END)
    text_result.insert(tk.END, report)


window = tk.Tk()
window.title("Статистика учнів")
window.geometry("600x400")
window.resizable(False, False)
window["bg"] = "#F19CBB"

label = tk.Label(
    window,
    text="Статистика учнів",
    font=("Arial", 20),
    bg="#F19CBB"
)
label.pack(pady=20)

label_info = tk.Label(
    window,
    text="Введіть кількість оцінок (1–20):",
    font=("Arial", 12),
    bg="#F19CBB"
)
label_info.pack(pady=5)

entry = tk.Entry(window, font=("Arial", 14))
entry.pack(pady=10)

button = tk.Button(
    window,
    text="Сформувати звіт",
    font=("Arial", 12),
    bg="lightgreen",
    command=create_report
)
button.pack(pady=10)

text_result = tk.Text(
    window,
    width=70,
    height=10,
    font=("Arial", 10)
)
text_result.pack(pady=10)

window.mainloop()