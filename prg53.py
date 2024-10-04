# Функции (encapsulation - инкапсуляция)
# Возвращаемое значение
def odd_even(num: int) -> str:
    """
    Функция возвращающая чёт или нечёт
    :param num: целое число
    :return: строку в которой "чёт" или "нечёт"
    """
    if not isinstance(num, int):
        return 'Ну ты даёшь!!!'
    if num % 2:
        return 'нечёт'
    return 'чёт'


# вызов
res = odd_even(5)
print(res)
