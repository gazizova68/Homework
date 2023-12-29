class Calculator:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

    def __sub__(self, other):
        return self.value - other.value

    def __mul__(self, other):
        return self.value * other.value

    def __truediv_(self, other):
        if other.value != 0:
            return self.value / other.value
        else:
            return "Ошибка: деление не производится на 0"


num1 = Calculator(10)
num2 = Calculator(5)

result_add = num1 + num2
result_sub = num1 - num2
result_mul = num1 * num2
# result_div = num1 / num2

print(f"Сумма: {result_add}")
print(f"Разница: {result_sub}")
print(f"Умножение: {result_mul}")
# print(f"Деление: {result_div}")
