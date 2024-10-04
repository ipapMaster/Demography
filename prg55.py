# Обработка исключений
def f_open(name: str) -> str:
    """
    Читает текстовый файл и
    возвращает его содержимое
    :param name: имя файла на чтение
    :return: содержимое файла
    """
    try:
        with open(name, encoding='UTF-8') as f:
            return f.read()
    except FileNotFoundError:
        with open(name, 'w', encoding='UTF-8') as f:
            f.write('Файл был заново создан!')
        return f'Файл {name} не существует или удалён! Был пересоздан'


res = f_open('example.txt')
print(res)
