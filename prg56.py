# Обработка исключений

# try (начало обработки)
# здесь выполняется "попытка" какого-либо действия
# except (собственно обработчик)
# исключение обрабатывается
# finally (не обязательная)
# программа продолжается с этого места,
# независимо от того, было исключение или нет
# else
# Если не было исключения

def divide():
    a = input('Введите А: ')
    b = input('Введите B: ')
    try:
        temp = float(a) / float(b)
        return temp
    except ZeroDivisionError:
        return 'Не делите на ноль'
    except Exception as exp:
        return f'Вот такое вот: {exp}'
    # except ValueError:
    #     return 'Нужно вводить только числа'


print(divide())
