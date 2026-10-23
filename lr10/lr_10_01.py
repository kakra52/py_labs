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

student1 = Student("Anna Ivanenko", "IT-10")
student2 = Student("Ivan Petrenko", "IT-10")

print(student1.info())
print(student2.info())