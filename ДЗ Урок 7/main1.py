# Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()), который должен принимать данные (список списков) для формирования матрицы.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.

class Matrix():
    def __init__(self, matrix: list) -> None:
        self.__matrix = matrix

    def __str__(self) -> str:
        return '\n'.join(((' '.join((str(col) for col in row))) for row in self.__matrix))

    def __add__(self, other):
        matrix = []
        for row in range(0, len(self.__matrix)):
            matrix.append([0 for _ in self.__matrix[row]])
            for col in range(0, len(self.__matrix[row])):
                matrix[row][col] = self.__matrix[row][col] + other.__matrix[row][col]
        return Matrix(matrix)


m1 = Matrix([[31, 32], [37, 43], [51, 86]])
m2 = Matrix([[1, 2], [3, 4], [5, 6]])
print(m1 + m2)
