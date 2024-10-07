# Модули
# import functions as f
from functions import *


def main():
    # Глобальные
    try:
        first = input('Введите первое число: ')
        second = input('Введите второе число: ')
        # Завтра продолжим

        print(summ(first, second))
        print(sub(first, second))
        print(divide(first, second))
        print(multiply(first, second))
    except:
        pass


# Если это главный исполняемый модуль
if __name__ == '__main__':
    main()
