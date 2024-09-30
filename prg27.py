# index - порядковый номер элемента в последовательности
# slice - срез [start:stop:step]
s = 'Python'

print(s[::-1])  # разворот строки срезом

length = len(s)  # для индекса отнимаем 1
print('Длина строки', s, length)

for ch in s:
    print(ch, end='')
