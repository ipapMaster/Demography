# Модули
# import functions as f
from functions import *


def main():
    # Глобальные
    try:
        first = float(input('Введите первое число: '))
        second = float(input('Введите второе число: '))

        print(summ(first, second))
        print(sub(first, second))
        print(divide(first, second))
        print(multiply(first, second))
    except ValueError:
        print('Работаю только с числами')
        return


# Если это главный исполняемый модуль
if __name__ == '__main__':
    main()
