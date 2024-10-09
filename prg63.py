# Объектно-ориентированный подход
# Инкапсуляция
# private __ - доступ извне напрямую закрыт
# public - доступ открыт всем и для всех
# protected _ - доступ только для членов производного класса
class Man:
    # Спец. методы
    def __init__(self, n='noname', a=0):  # Конструктор
        # Поля класса (члены класса)
        self.name = n
        self.age = a
        self.non_legal_names = ['Васёк', 'Павло', 'Павлик']

    # Методы класса
    def info(self):
        print(f'{self.name}, возрастом {self.age}')

    # Геттеры (getters)
    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    # Сеттеры (setters)
    def set_age(self, new_age):
        if new_age < 0:
            self.age = -new_age
        else:
            self.age = new_age

    def set_name(self, new_name):
        if new_name not in self.non_legal_names:
            self.name = new_name
        print('Имя недопустимо, замены не было.\n'
              'Список запрещённых имён', end=': ')
        self.print_non_legal_names()

    def print_non_legal_names(self):
        print(*self.non_legal_names, sep=', ')


dima = Man('Дмитрий', 17)
# dima.age = 18  # так не корректно
dima.set_name('Павлик')
dima.set_age(-18)  # так корректно
n = dima.get_name()
print(n)
# dima.info()
