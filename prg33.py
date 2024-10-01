# Операции со списками и методы списков
# print(dir([]))
okroshka = ['огурец', 'квас', 'кефир', 'соль', 'перец']
additional = ['колбаса', 'редис', 'картофель']

final = okroshka + additional + ['петрушка']
final.append('укроп')  # final += ['укроп']
temp = final.pop(2)
print(temp)
final.remove('соль')
final.insert(4, temp)
print(final.index('перец'))
# final.clear()
print(final)

# Способ №1
# print('Ингредиентов в окрошке:', len(final))
# print('Вот они:')
# count = 1
# for item in final:
#     print(f'\t{count}. {item}')
#     count += 1

# Способ №2
# print('Ингредиентов в окрошке:', len(final))
# print('Вот они:')
# final.sort()
# for item in range(len(final)):
#     print(f'\t{item + 1}. {final[item]}')

# Способ №3
print('Ингредиентов в окрошке:', len(final))
print('Вот они:')
final.sort()
print(*final)
