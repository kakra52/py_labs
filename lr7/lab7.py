from pathlib import Path

BASE = Path(__file__).resolve().parent


def task1():
    with open(BASE / 'text.txt', 'r', encoding='utf-8') as file:
        text = file.read()

    lines = text.splitlines()
    words = sum(len(line.split()) for line in lines)
    print('Завдання 1')
    print(f'Рядків: {len(lines)}')
    print(f'Слів: {words}')
    print(f'Символів: {len(text)}')
    if lines:
        number, longest = max(enumerate(lines, start=1), key=lambda item: len(item[1]))
        print(f'Найдовший рядок: №{number}, {len(longest)} символів')
        print(f'Текст: {longest}')
    else:
        print('Файл порожній.')


def task2():
    fragment = input('\nЗавдання 2. Введіть фрагмент: ').strip()
    if not fragment:
        print('Фрагмент не може бути порожнім.')
        return

    found = False
    with open(BASE / 'text.txt', 'r', encoding='utf-8') as file:
        for number, line in enumerate(file, start=1):
            if fragment.casefold() in line.casefold():
                print(f'{number}: {line.rstrip(chr(10) + chr(13))}')
                found = True
    if not found:
        print('Збігів не знайдено.')


def task3():
    students = []
    with open(BASE / 'students.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            name, score_text = line.split(';')
            score = int(score_text)
            if score > 80:
                students.append((name, score))

    students.sort(key=lambda student: student[1], reverse=True)
    with open(BASE / 'result.txt', 'w', encoding='utf-8') as file:
        for name, score in students:
            file.write(f'{name};{score}\n')
    print(f'\nЗавдання 3. У result.txt записано {len(students)} студентів.')


def task4():
    grades = {}
    with open(BASE / 'grades.csv', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            name, subject, grade_text = line.split(';')
            grades.setdefault(name, []).append(int(grade_text))

    results = []
    for name, scores in grades.items():
        average = sum(scores) / len(scores)
        results.append((name, len(scores), average))
    results.sort(key=lambda item: (-item[2], item[0]))

    with open(BASE / 'report.txt', 'w', encoding='utf-8') as file:
        for name, count, average in results:
            file.write(f'{name} — оцінок: {count} — середній: {average:.2f}\n')
        if results:
            best_average = results[0][2]
            winners = [name for name, _, average in results if abs(average - best_average) < 1e-9]
            file.write(f'Найкращий результат: {" та ".join(winners)} — {best_average:.2f}\n')
        else:
            file.write('Немає даних про оцінки.\n')
    print('Завдання 4. Звіт збережено у report.txt.')


def main():
    task1()
    task2()
    task3()
    task4()


if __name__ == '__main__':
    main()
