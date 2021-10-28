# Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.
def divide(num, den):
    try:
        return num / den
    except ZeroDivisionError:
        return


def get_number(msg):
    while True:
        try:
            return float(input(msg).strip())
        except ValueError:
            continue


print(divide(get_number("Введите числитель "), get_number("Введите знаменатель ")))
