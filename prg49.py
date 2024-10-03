# Чтение нескольких строк (способ №1)
fo = open('sample.txt', encoding='UTF-8')  # по умолчанию режим rt
# print(dir(fo))
text = fo.readline()
while text != '':  # если строка существует
    print(text, end='')
    text = fo.readline()
fo.close()  # открытый файл обязательно закрывать
