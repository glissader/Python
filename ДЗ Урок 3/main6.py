# Реализовать функцию int_func(), принимающую слова из маленьких латинских букв и возвращающую их же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text.

def int_func(*s):
    result = []
    for item in s:
        result.append(item.lower().title())
    return result


print(int_func("text", "soMe"))
