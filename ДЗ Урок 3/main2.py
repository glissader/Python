# Выполнить функцию, которая принимает несколько параметров,
# описывающих данные пользователя: имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Осуществить вывод данных о пользователе одной строкой.
def user(firstname, lastname, birth_year, city, email, phone):
    print(f'{firstname} {lastname} ({birth_year}), {city}, {email}, {phone}')


user(firstname="Vladimir", lastname="Savostyanov", birth_year=1976, city='Moscow', email="v@none.com",
     phone='123-12-12')
