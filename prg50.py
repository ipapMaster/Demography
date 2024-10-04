# Чтение нескольких строк (способ №2)
fo = open('sample.txt', encoding='UTF-8')  # по умолчанию режим rt
# print(dir(fo))
# text = fo.readline()  # читает одну строку \n
# while text != '':  # если строка существует
#     print(text, end='')
#     text = fo.readline()
text = fo.readlines()  # читает все строки файла в список
print(text)
fo.close()  # открытый файл обязательно закрывать
