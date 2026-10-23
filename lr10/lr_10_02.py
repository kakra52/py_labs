class Person:
    def __init__(self, name):
        self.name = name

    def info(self):
        return f"Ім'я: {self.name}"

class Student(Person):
    def __init__(self, name, group):
        super().__init__(name)
        self.group = group

    def info(self):
        return f"Учень: {self.name}, група: {self.group}"

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject

    def info(self):
        return f"Викладач: {self.name}, предмет: {self.subject}"

people = [
    Person("Ivan Komarov"),
    Student("Anna Ivanenko", "IT-10"),
    Student("Petro Sydorenko", "IT-12"),
    Teacher("Olena Kovalenko", "Python")
]

for person in people:
    print(person.info())
