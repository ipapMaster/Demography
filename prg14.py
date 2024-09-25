# Цикл While
# count /= 1 тоже, что и count = count / 1
# count *= 1 тоже, что и count = count * 1
# count -= 1 тоже, что и count = count - 1
# count += 1 тоже, что и count = count + 1

import turtle as t

sides = 6
dist = 50
angle = 360 / sides
count = 0  # счётчик числа "витков" цикла
sq_count = 0  # счетчик числа сторон квадрата

t.speed(0)

while count < sides:
    sq_count = 0  # обнуляем счётчик сторон квадрата
    while sq_count < 4:  # внутренний
        t.forward(dist)  # (вложенный) цикл
        t.right(90)
        sq_count += 1
    t.right(angle)
    count += 1  # инкремент счётчика вн. цикла (увеличение на 1)

t.mainloop()
