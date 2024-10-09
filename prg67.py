# Доп. библиотека PIL (pillow)
from PIL import Image, ImageFilter

# пробуем прочитать файл original.jpg
try:
    orig = Image.open('original.jpg')
except FileNotFoundError:
    print('Файл не найден')

print('Параметры считано файла:')
print(f'Формат: {orig.format}')
print(f'Размеры: {orig.size}')
print(f'Цветовая схема: {orig.mode}')

w, h = orig.size  # получили и распаковали кортеж
pixels = orig.load()  # список пикселей [x, y]

for x in range(w):
    for y in range(h):
        r, g, b = pixels[x, y]
        average = (r + g + b) // 3
        pixels[x, y] = average, average, average

orig.save('grayscale.jpg')

blur = orig.filter(ImageFilter.GaussianBlur(2))
cropped = orig.crop((0, 0, 300, 400))
contour = orig.filter(ImageFilter.CONTOUR)
cropped.save('cropped.jpg')
blur.save('blur.jpg')
contour.save('contour.jpg')
