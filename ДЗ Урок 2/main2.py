# Для списка реализовать обмен значений соседних элементов.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д.
# При нечётном количестве элементов последний сохранить на своём месте.
# Для заполнения списка элементов нужно использовать функцию input().

in_str = input("Введите элементы, разделенные пробелом ")
result_list = in_str.strip().split(" ")
print(result_list)
for idx in range(0, len(result_list) - 1, 2):
    result_list[idx], result_list[idx + 1] = result_list[idx + 1], result_list[idx]
print(result_list)