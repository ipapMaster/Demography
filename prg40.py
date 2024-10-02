# Операции между кортежами и другими объектами
s = 'Python'
# s = (255, 128, 64)
print(len(s))
lst = ['бремя', 'время', 'стремя']
# Функция sorted() сортирует
# итерируемую последовательность
# и возвращает в виде списка
# temp = list(enumerate(lst))
print('Существительные:')
for index, value in enumerate(lst):
    print(f'\t{index + 1}. {value}')
