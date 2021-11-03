# Реализовать проект «Операции с комплексными числами».
# Создайте класс «Комплексное число», реализуйте перегрузку методов сложения и умножения комплексных чисел.
# Проверьте работу проекта, создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата.

class Complex:
    __re: float
    __im: float

    def __init__(self, re: float, im: float):
        self.__re = re
        self.__im = im

    def __add__(self, other: 'Complex'):
        return Complex(
            self.__re + other.__re,
            self.__im + other.__im
        )

    def __mul__(self, other: 'Complex'):
        r1 = self.__re * other.__re
        r2 = self.__im * other.__im
        i1 = self.__re * other.__im
        i2 = self.__im * other.__re
        return Complex(r1 - r2, i1 + i2)

    def __str__(self):
        return f"({self.__re}{'+' if self.__im > 0 else ''}{self.__im}i)"


a = Complex(1, 2)
b = Complex(2, 1)
print(a + b)
print(a * b)
