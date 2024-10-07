# Утверждение (assertion)

length = 3

try:
    text = input('Введите любой текст: ')
    assert len(text) > length  # утверждение
    print(f'Вы ввели: {text}.')
except AssertionError:
    print(f'Нет. Ваш текст короче, чем {length} символа.')
