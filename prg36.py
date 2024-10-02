# Методы списков и строк
# print(dir([]))
okroshka = ['огурец', 'квас', 'кефир', 'соль', 'перец']
additional = ['колбаса', 'редис', 'картофель']

final = okroshka + additional + ['петрушка']
final.append('укроп')  # final += ['укроп']

# Способ №3
print('Ингредиентов в окрошке:', len(final))
print('Вот они:', end='')
final.sort()
print('\t', *final, sep='\n\t')

s = 'Сабака'

n = s.replace('а', 'о', 1)
