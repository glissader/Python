# Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить её на экран.

import random

n = (random.random() for _ in range(0, random.randrange(1, 10)))
with open(r'out5.txt', 'w') as f_out:
    print(*n, file=f_out)

with open(r'out5.txt', 'r') as f_out:
    print(sum((float(i) for i in f_out.readline().split())))
