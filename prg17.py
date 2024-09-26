# Введение в цикл for
# s - start (по умолчанию ноль, включая)
# s - stop (не включая)
# s - step (шаг - по умолчанию - 1)
# range(start, stop, step)

# for <переменная> in range(начало, финиш, шаг)

# Первый способ
for x in range(4, 50, 10):
    print(x)

# Второй способ
for x in range(1, 51):
    if x % 10 == 4:
        print(x)
