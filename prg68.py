# Доп. библиотека PIL (pillow)
from PIL import ImageDraw, Image, ImageFont

# создаём и рисуем
# 1 холст
canvas = Image.new("RGB", (200, 200), (0, 0, 200))

# создаём рисовальщик
draw = ImageDraw.Draw(canvas)

# рисуем линии окна
draw.line((100, 0, 100, 200), fill='brown', width=5)
draw.line((0, 100, 200, 100), fill='brown', width=5)

# рисуем прямоугольник
draw.rectangle((0, 0, 200, 200), outline='brown', width=5)
draw.ellipse((0, 0, 200, 200), outline='brown', width=5)

# напишем текст
text = 'Окно'
f = ImageFont.truetype('arial.ttf', size=28)
draw.text((80, 90), text, font=f)

# рисуем полигон (треугольник)
# draw.polygon(
#     xy=(
#         (200, 200),
#         (150, 200),
#         (200, 150)
#     ), fill='red', outline=(0, 0, 0)
# )

# сохраняем
canvas.save('line.png', 'PNG')
