# Файлы (запись нескольких строк в файл)
# Бывают текстовые или бинарные (двоичные)
# Режимы (mode): r - read, w - write, a - append
# Подрежим: b - binary, t - text
# UTF-8 - Unicode Text Format (256 - ASCII)
total = 0
fo = open('sample.txt', 'wt', encoding='UTF-8')  # по умолчанию режим rt
# fo.write('\n')  # перевод на новую строку
num = fo.write('Это первая строка внутри файла\n')
total += num
num = fo.write('Это вторая строка внутри файла')
total += num
print(f'В файл {fo.name} записано {total} байт (символов).')
fo.close()  # открытый файл обязательно закрывать
