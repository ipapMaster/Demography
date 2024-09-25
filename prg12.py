# сложное условие (логическое "ИЛИ")
# AND, а потом OR
string = ''  # пустая строка

name = input('Как Ваше имя: ')
surname = input('Как Ваша фамилия: ')
age = input('Ваш возраст: ')
gender = input('Укажите пол (М или Ж): ')

if name == 'Вася' and surname == 'Пупкин':
    print('Уважайте Ваше имя!!!')
else:
    # основное условие
    if (gender == 'М' or gender == 'м'
            or gender == 'v' or gender == 'V'):
        string = 'Уважаемый '
    elif (gender == 'Ж' or gender == 'ж'
          or gender == ';' or gender == ':'):
        string = 'Уважаемая '
    else:
        string = 'Уважаемый товарищ '

    string = (string + name + ' ' + surname + ' ' +
              'Ваш возраст: ' + age + '.')
    ##################

print(string)
