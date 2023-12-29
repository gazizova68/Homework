class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def __moneyX__(self):
        money = float(input("Введите нужную сумму для пополнения вашего счета: "))
        self._balance += money
        print(f"Ваш баланс после поплнения составляет: {self._balance}")

    def __kill__(self):
        self._balance = 0
        print("Ваш баланс обнулен")

    def __jackpot__(self):
        self._balance *= 10
        print(f"Вы везунчик! Ваш баланс увеличен в 10 раз! И составляет: {self._balance}")

    def __merge_balance__(self, other_account):
        self._balance += other_account._balance
        other_account._balance = 100
        print(f"Ваш баланс и баланс соперника объединены. И только ваш текущий баланс составляет: {self._balance}")


account1 = Bank("Mika's Account", 100)
account2 = Bank("Kama's Account", 100)

account1.__moneyX__()
account1.__jackpot__()
account1.__merge_balance__(account2)

print(f"{account1._name}'s balance: {account1._balance}")
print(f"{account2._name}'s balance: {account2._balance}")
