# Программа принимает действительное положительное число x и целое отрицательное число y.
# Выполните возведение числа x в степень y. Задание реализуйте в виде функции my_func(x, y).
# При решении задания нужно обойтись без встроенной функции возведения числа в степень.

# Подсказка: попробуйте решить задачу двумя способами.
# Первый — возведение в степень с помощью оператора **.
# Второй — более сложная реализация без оператора **, предусматривающая использование цикла.

def my_func1(x, y):
    return x ** y


def my_func2(x, y):
    result = 1
    for _ in range(0, abs(y)):
        result *= x
    return 1.0 / result if y < 0 else result


x = 0
while x <= 0:
    try:
        x = float(input("x = ").strip())
    except ValueError:
        continue

y = 0
while y >= 0:
    try:
        y = int(input("y = ").strip())
    except ValueError:
        continue

print(my_func1(x, y))
print(my_func2(x, y))
