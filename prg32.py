# Списки - iterable object, mutable-изменяемый тип коллекции

s = {'a', 1, 36.6}  # множество
empty_set = set()
array = []  # пустой список
array = list()  # пустой список
# index     0         1        2
array = ['ясно', 'пасмурно', 36.6]
okroshka = ['огурец', 'квас', 'кефир', 'соль', 'перец']

print(okroshka[0:len(okroshka):2])  # [::2]

word = 'pithon'  # immutable
# word[1] = 'y' - так нельзя
lst = list(word)

print(lst)

lst[1] = 'y'

print(*lst, sep='')

dishes = ['борщ', 'пюре', 'компот', 'сок']
# first, second, third = dishes
first, second, *drink = dishes

print(drink)
