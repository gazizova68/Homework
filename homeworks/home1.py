class Home:
    new = True


home = Home

n = input("Введите число: ")
try:
    n = int(n)
    print("Верный ввод")
except ValueError:
    print("Вводите только целые числа!")
