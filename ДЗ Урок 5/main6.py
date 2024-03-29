# Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных, практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}

with open(r'in6.txt', 'r') as f_in:
    kw = {s[0]: s[1] for s in (s.strip().split(':') for s in f_in.readlines())}
    kw_out = {}
    for k, v in kw.items():
        values = "".join(filter(lambda x: x in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ' '), v)) \
            .strip().split()
        total = sum((int(i) for i in values))
        kw_out.update({k: total})
    print(kw_out)
