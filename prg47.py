# Файлы (чтение)
# Бывают текстовые или бинарные (двоичные)
# Режимы (mode): r - read, w - write, a - append
# Подрежим: b - binary, t - text
# UTF-8 - Unicode Text Format (256 - ASCII)
fo = open('sample.txt', 'rt', encoding='UTF-8')  # по умолчанию режим rt
print(fo.name, fo.mode, fo.encoding)
text = fo.read()
fo.close()  # открытый файл обязательно закрывать

lst = text.split()

# как извлечь нужный фрагмент из текста (способ №1)
if 'внутри' in lst:
    for word in lst:
        if word == 'внутри':
            print(word)
else:
    print('Такого слова в файле нет')

# как извлечь нужный фрагмент из текста (способ №2)
if 'внутри' in lst:
    index = lst.index('внутри')  # метод списка index
    print(lst[index])
else:
    print('Такого слова в файле нет')
