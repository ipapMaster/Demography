# Управление циклом с помощью break и continue
for x in range(5):
    if x == 2:
        break
    #else:
    #    continue - так делать не надо
    print(x)
else:
    print('Нормальное завершение цикла')

# Выведите элементы строки без пробелов
string = 'О сколько2!'

for letter in string:
    if letter == '2':
        break
    print(letter, end='')
print()