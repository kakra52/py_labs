class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Помилка: сума поповнення має бути більшою за 0.")
        else:
            self.balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            print("Помилка: сума списання має бути більшою за 0.")
        elif amount > self.balance:
            print(f"Помилка: недостатньо коштів для -{amount}")
        else:
            self.balance -= amount

    def info(self):
        print(f"{self.owner}: баланс {self.balance}")


account1 = BankAccount("Ivan", 1000)
account2 = BankAccount("Olha", 700)

account1.deposit(500)
account1.withdraw(300)
account1.withdraw(2000)
account1.deposit(0)
account1.withdraw(-50)

account2.withdraw(200)
account2.deposit(100)
account2.deposit(-50)
account2.withdraw(0)

print("\nПідсумковий стан рахунків:")
account1.info()
account2.info()
