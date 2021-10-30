# Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
# Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
# Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.

# example to run:
# python main1.py 160 44 10
from sys import argv

script_name, output_hours, rate_per_hour, premium = argv
salary = float(output_hours) * float(rate_per_hour) + float(premium)
print(f'{salary}')
