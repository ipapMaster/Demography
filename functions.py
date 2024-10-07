# Функции моего калькулятора


def summ(a, b):
    """
    Сумма двух чисел
    :param a: любое
    :param b: число
    :return: сумма
    """
    try:
        res = a + b
    except TypeError:
        return 'Складываю только числа'
    else:
        return res


def sub(a, b):
    """
    Разность двух чисел
    :param a: любое
    :param b: число
    :return: разность
    """
    try:
        res = a - b
    except TypeError:
        return 'Вычитаю только числа'
    else:
        return res


def divide(a, b):
    """
    Частное двух чисел
    :param a: любое
    :param b: число
    :return: частное
    """
    try:
        res = a / b
    except TypeError:
        return 'Делю только числа'
    except ZeroDivisionError:
        return 'На ноль делить нельзя'
    else:
        return res


def multiply(a, b):
    """
    Произведение двух чисел
    :param a: любое
    :param b: число
    :return: произведение
    """
    try:
        res = a * b
    except TypeError:
        return 'Умножаю только числа'
    else:
        return res


if __name__ == '__main__':
    print('Не запускай меня. Это библиотека функций.')
