# Создать текстовый файл in2.txt (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.

with open(r'in2.txt', 'r') as f_obj:
    lines_count = 0
    for line in (l.strip() for l in f_obj.readlines()):
        lines_count += 1
        words_count = len(line.split())
        print(f'Количество слов {words_count} в строке "{line}"')
    print(f'Количество строк: {lines_count}')
