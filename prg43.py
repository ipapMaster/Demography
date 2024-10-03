# Словари
# d = dict()  # пустой словарь
# d = {}  # пустой словарь
d = {
    'стул': 'chair',
    'стол': 'table',
    'яблоко': 'apple',
    'меню': ['суп', 'тефтели', 'чай'],
}
# print(dir(d))
# print(d['стол'])
d['слива'] = 'plum'
d[0] = 'one'
d[36.6] = 'normal'
d[True] = 'Истина'
print(len(d))
print(list(d.keys()))  # список ключей словаря
print(list(d.values()))  # список значений словаря
print(list(d.items()))  # список кортежей (пар) (ключ, значение)
if 'Истина' in d.values():
    print('Истина есть среди значений')
for key in d.keys():
    print(f'Ключ: {key}, Значение: {d[key]}')
for key, value in d.items():
    if value == 'Истина':
        print(f'Для Истина ключ - {key}')
    # print(f'Ключ: {key}, Значение: {value}')
# print(d[True])
print(d.get('груша', 0))
del d['стул']
print(d)
