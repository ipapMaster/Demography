# Кортежи - тот же список, но не изменяемый
# В отличии от списка занимает меньше места в памяти
# В -"-"- обращение к нему происходит быстрее
# Константы пишутся заглавными буквами (PEP8)
G = 9.81
PI = 3.14
BLACK = (0, 0, 0)
RED = (255, 0, 0)
red = [255, 0, 0]
print(RED.__sizeof__())
print(red.__sizeof__())
print(RED.index(255))
print(RED.count(0))

# Кортежи конкатенируются
result = BLACK + RED
empty_tuple = tuple()
num = (1,)  # кортеж из одного элемента

# print(dir(num))

a = 5
b = 2

print(a, b)

#  Классический способ
#  замены значений двух переменных
# temp = b
# b = a
# a = temp

a, b = b, a

print(a, b)

# Список из кортежей
cards = [('Дама', 'Червей'), ('Туз', 'Пик')]

print(cards[0][0], cards[0][1])
print(*cards[0], sep=', ')

# text = '   О    сколько    нам    открытий    чудных    '
# lst = text.split()
# print(lst)
# res = ' '.join(lst)
# print(res)
