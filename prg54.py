# Функции (encapsulation - инкапсуляция)
# Область видимости переменных
# Global scope

b = 5


def calc(x: int = 1, y: int = 0) -> int:
    # local scope
    a = 3
    res = 2 * x + y + a
    return res


def multy(*args: int) -> int:
    """
    Функция вычисления произведения
    переменно числа аргументов
    :param args: ноль или несколько целых чисел
    :return: произведение аргументов
    """
    if len(args) == 0:
        return 0
    if len(args) == 1:
        return args[0]
    res = 1
    for i in range(len(args)):
        res *= args[i]
    return res


def increment():
    global b
    b += 1


print(multy(1, 2, 5, 8))
increment()
result = calc(b)
# garbage collector - сборщик мусора
print(result)
