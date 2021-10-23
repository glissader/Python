# Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма.
# Например, прибыль — выручка больше издержек, или убыток — издержки больше выручки.
# Выведите соответствующее сообщение.
# Если фирма отработала с прибылью, вычислите рентабельность выручки.
# Это отношение прибыли к выручке.
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы в расчёте на одного сотрудника.

profit = float(input("введите выручку  в тыс. "))
expenses = float(input("введите издержки в тыс. "))
if profit > expenses:
    print("прибыль")
    rent = (profit - expenses) / profit
    print(f'рентабельность выручки {rent * 100:.3f} %')

    staff = int(input("введите число сотрудников "))
    profit_staff = (profit - expenses) / staff
    print(f'прибыль в расчёте на одного сотрудника {profit_staff:.3f} тыс.')
elif profit < expenses:
    print("убыток")
else:
    print("0")
