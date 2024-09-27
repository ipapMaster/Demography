# Виды коллекций в Python (итерируемые):
# 1. множества - set()
# 2. списки - list() -> []
# 3. кортежи - tuple()-> ()
# 4. словари - dictionary -> dict() -> {}

# Множество - неупорядоченная структура данных
# Множество не содержит повторов
empty_set = set()  # пустое множество
# num_set = {1, 2, 3, 'Строка', 36.6, True, False}
num_set = {1, 2, 3}
letter_set = {'a', 'b', 'c', 'c', 'a'}

error_method = set('1, 2, 3')
print(error_method)

letter_set.add('d')
letter_set.add('a')

print(letter_set)

# letter_set.pop() # случайное удаление элемента
# letter_set.remove('e') # удаление конкретного элемента с проверкой
letter_set.discard('a')  # удаление в слепую

print(letter_set)

word = 'молоток'
if 'о' in word:
    print('Да')
letter_in_word = set(word)

print(letter_in_word)
