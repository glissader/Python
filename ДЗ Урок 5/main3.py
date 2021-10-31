# Создать текстовый файл (не программно).
# Построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тысяч, вывести фамилии этих сотрудников. Выполнить подсчёт средней величины дохода сотрудников.
# Пример файла:
# Иванов 23543.12
# Петров 13749.32

with open(r'in3.txt', 'r') as f_obj:
    kv = {s[0]: float(s[1]) for s in (s.strip().split() for s in f_obj.readlines())}
    less20 = [k for k in kv if kv.get(k) < 20000.0]
    average = sum((k for k in kv.values())) / len(kv)
    print(f'Оклад менее 20 тыс. рублей: {less20}')
    print(f'Среднй доход сотрудника: {average:.2f}')
