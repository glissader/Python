# Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
# В рамках класса реализовать два метода.
# Первый, с декоратором @classmethod, должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
# Проверить работу полученной структуры на реальных данных.

class Date:
    __day: int
    __month: int
    __year: int

    def __init__(self, date_string: str) -> None:
        numbers = Date.extract(date_string)
        Date.validate(numbers)
        self.__day, self.__month, self.__year = numbers

    def __str__(self) -> str:
        return f'{self.__day:02}.{self.__month:02}.{self.__year:04}'

    @classmethod
    def extract(cls, date_string: str) -> tuple:
        return *(int(x) for x in date_string.split('-')),

    @staticmethod
    def validate(numbers: tuple):
        dd, mm, yyyy = numbers
        assert 1 <= dd <= 31, "invalid Date"
        assert 1 <= mm <= 12, "invalid Month"
        assert 1970 <= yyyy <= 2100, "Invalid Year"


print(Date('03-10-2021'))
