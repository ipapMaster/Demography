# "Бросаемся" исключениями (throw (Java, C++, C#) -> raise)
min_val = 1
max_val = 10

try:
    cur_val = int(input(f'Введите целое число от {min_val} до {max_val}: '))
    if cur_val == 0:
        raise ValueError('ноль вводить нельзя!!!')
    if not min_val <= cur_val <= max_val:
        raise ValueError(f'введенное число вне диапазона ({min_val}...{max_val}).')
    print(f'Да! Всё верно. Число {cur_val} '
          f'лежит в диапазоне от {min_val} до {max_val} ')
except ValueError as exp:
    print('Надо быть повнимательнее:', exp)

