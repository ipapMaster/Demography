# Итерируемый объект (iterable object)
# и первые операции с ним
# int и float не являются итерируемым объектом

string = 'абвгдейка'

for symbol in string:
    print(symbol)

string2 = 'Вася Пупкин'

if 'Пупкин' in string2:
    print('Не надо писать:', '"' + string2 + '"')
