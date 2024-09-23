import turtle as t  # подключили "черепашку"

# RAM - random access memory
# DRY - do not repeat yourself (code should be clear)
sides_of_figure = 8  # число сторон замкнутой фигуры
dist = 120  # переменной dist присвоено значение 150
angle = 360 / sides_of_figure  # угол, как 360 / sides

t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)
t.forward(dist)
t.right(angle)

t.mainloop()
