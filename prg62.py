# Объектно-ориентированный подход
# Инкапсуляция
class Ball:
    # Спец. методы
    def __init__(self, diametr=1, color='жёлтый'):
        # Поля класса (члены класса)
        self.diametr = diametr
        self.color = color

    # Методы класса
    def info(self):
        print('Мяч имеет цвет: ', self.color)
        print('Размер мяча : ', self.diametr)


ball1 = Ball(5, 'красный')  # ball1 - экземпляр класса Ball #1
ball2 = Ball(10, 'синий')   # ball2 - экземпляр класса Ball #2
ball3 = Ball()
ball4 = Ball()

print(id(ball1))
print(id(ball2))
print(id(ball3))
print(id(ball4))

# ball1.info()
# ball2.info()
# ball3.info()
# ball4.info()
# print(ball1.color, ball1.diametr)
# print(ball2.color, ball2.diametr)
