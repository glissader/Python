# Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Напишите программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

words = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}
with open(r'out4.txt', 'w') as f_out:
    with open(r'in4.txt', 'r') as f_obj:
        for l in f_obj.readlines():
            en = l.strip().split()[0]
            l = l.replace(en, words.get(en.lower()).capitalize()).strip()
            print(l, file=f_out)
