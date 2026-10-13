import math
from math import *
import statistics as stat
import random
from datetime import date
from tkinter import *


def text():
    lbl_text['text'] = 'hello world'


def clear(event):
    lbl_text['text'] = ''


# print(math.sqrt(81))
#
# a = [10, 15, 3, 5, 8, 9]
# print(f'Середній бал: {stat.mean(a)}')
#
# r = int(input("r ="))
# circle_area = round(pi * pow(r, 2), 2)
# print(circle_area)
#
# balls = 25
# n = 6
# print(f'Повністю заповнених коробок: {floor(balls / n)}')
# print(f'Всього коробок: {ceil(balls / n)}')
#
# numbers = []
# for i in range(10):
#     numbers.append(random.randint(1, 100))
# print(f'Випадкові 10 чисел: {numbers}')
#
# selected = random.choice(numbers)
# print(f'Випадкове число: {selected}')
# print(f'Сьогодні: {date.today()}')


# Створення вікна
window = Tk()
window.title('my first window')
window.geometry('500x400')
window.resizable(False, False)
window["bg"] = "#F19CBB"


# Заголовок
label = Label(
    window,
    text="Супер-пупер програма",
    font=("Arial", 18),
    bg="#F19CBB",
    pady=20
)
label.pack()


# Рамка для кнопок
frame = Frame(window, bg="#F19CBB")
frame.pack()


# Перша кнопка
bt1 = Button(
    frame,
    text="OK",
    width=7,
    activebackground="lightgreen",
    command=text
)
bt1.grid(row=0, column=0, padx=10)


# Друга кнопка
bt2 = Button(
    frame,
    text="OK",
    width=7,
    activebackground="lightgreen"
)
bt2.grid(row=0, column=1, padx=10)

bt2.bind("<Button-1>", clear)


# Напис під кнопками
lbl_text = Label(
    frame,
    text="",
    font=("Arial", 18),
    bg="#F19CBB",
    pady=20
)
lbl_text.grid(row=1, column=0, columnspan=2)


# Запуск програми
window.mainloop()