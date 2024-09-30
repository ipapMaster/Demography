# Пример задачи с множествами

forbiden = {'l', 'O', 'I'}
letters = {'a', 'b', 'c', 'd', 'l', 'O', 'I'}
digits = {1, 2}

# удаляем некорректные символы
remove_incorrect = letters - forbiden

# объединяем с цифрами
temp = remove_incorrect | digits

temp = list(temp)

for i in range(6):
    print(temp[i], end='')  # [] - обратиться по индексу
