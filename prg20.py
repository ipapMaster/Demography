string = 'Телевизор'
# определение числа элементов итерируемого объекта
number = input('Введите целое число: ')
length = len(number)
# Число 5600 4-х значное
print('Число', number, str(length) + '-x', 'значное.')

total = 1

for item in number:
    total *= int(item)

print('Произведение разрядов числа',
      number, 'равно:', total)

