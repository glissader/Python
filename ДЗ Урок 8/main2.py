# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class CustomZeroDivisionError(Exception):
    def __str__(self) -> str:
        return 'Division By Zero'

    @staticmethod
    def check_zero_division(num: int, den: int) -> float:
        if den == 0:
            raise CustomZeroDivisionError
        else:
            return num / den


while True:
    try:
        num = int(input("Введите числитель ").strip())
        den = int(input("Введите знаменатель ").strip())
        print(f"Результат = {CustomZeroDivisionError.check_zero_division(num, den)}")
        break
    except CustomZeroDivisionError as e:
        print(e)
