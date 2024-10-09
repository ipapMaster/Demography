# Доп. библиотека PIL (pillow)
from PIL import ImageDraw, Image

# создаём и рисуем
# 1 холст
canvas = Image.new("RGB", (200, 200), (128, 128, 128))

# создаём рисовальщик
draw = ImageDraw.Draw(canvas)

# рисуем линию
draw.line((0, 0, 200, 200), fill=(255, 0, 0), width=3)

# сохраняем
canvas.save('line.png', 'PNG')
