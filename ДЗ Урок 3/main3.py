# Реализовать функцию my_func(), которая принимает три позиционных аргумента и возвращает сумму наибольших двух аргументов.
def my_func(a, b, c):
    return sum(sorted((a, b, c,), reverse=True)[:2])


print(my_func(1, 2, 3))
print(my_func(3, 1, 2))
print(my_func(-3, -1, -3))
