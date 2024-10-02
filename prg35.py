import string as s
import random as r

num = 5

# набор из букв и цифр
set_of_symbols = s.digits + s.ascii_uppercase + s.ascii_lowercase
# превращаем в множество
set_of_symbols = set(set_of_symbols)
# удаляем сомнительные символы
set_of_symbols = set_of_symbols - {'O', '0', '1', 'l', 'I'}
# множество больше не нужно, конвертируем в список
set_of_symbols = list(set_of_symbols)
# замешали полученный список
r.shuffle(set_of_symbols)
# берём первые num-символов (срезом)
# temp = set_of_symbols[:num]
# получаем случайные n-символов
# temp = [r.choice(set_of_symbols)]
# for _ in range(num):
#     temp.append(r.choice(set_of_symbols))
# случайная выборка в виде списка без повторов
temp = r.sample(set_of_symbols, k=num)
# print(temp)
# полученную строку превратили в список
# temp = list(temp)
# добавили спец. символы
temp += ['@', '!', '#', '$', '&', '?']
# и замешали с буквами и цифрами
r.shuffle(temp)
# проверяем, что спец. символ не стоит на 1-м месте
while temp[0] in ['@', '!', '#', '$', '&', '?']:
    r.shuffle(temp)
# объединяем все символы из списка в одну строку
password = ''.join(temp)
# выводим результат
print(password)
