# Цикличное выполнение программы
# Вечный цикл и flag


choice = ''  # инициализация выбора пользователя
work = True

while work:
    choice = input('Введите R - для поворота направо,'
                   'L - для поворота налево, или Q для выхода: ')
    if choice == 'L' or choice == 'l':
        print('Вы повернули налево: ', choice)
    elif choice == 'R' or choice == 'r':
        print('Вы повернули направо: ', choice)
    elif choice == 'Q':
        work = not work  # инвертировал булево значение
    else:
        print('Вы продолжили движение прямо: ', choice)
else:
    print('До свидания!')


