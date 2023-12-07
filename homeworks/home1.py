class Home:
    def __new__(cls, *args, **kwargs):
        return Home
    n = input("Введите число: ")
    try:
        n = int(n)
        print("Верный ввод")
    except ValueError:
        print("Вводите только целые числа!")


home = Home
