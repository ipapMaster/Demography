# Циклы, операторы и др.
import turtle as t

colors = ('red', 'green', 'blue', 'yellow', 'purple')

length = len(colors)
angle = 360 / length - 1

t.bgcolor('black')
t.speed(0)

for i in range(200):
    t.width(i // 100 + 1)
    t.color(colors[i % length])
    t.forward(i)
    t.right(angle)

t.mainloop()
