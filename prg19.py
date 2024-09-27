# # Стандартный вывод (stdout) - в консоль (print) con
# # Именованные аргументы: sep=' ' и end='\n'
# # Стандартный ввод (stdin) - с клавиатуры (input)
#
# # И смех, и слёзы, и любовь.
# print('И смех', 'слёзы', 'любовь', sep=', и ', end='.\n')
#
# """
# Сегодня в меню:
#     - суп
#     - пюре
#     - компот
# """
# print('Сегодня в меню:', 'суп', 'пюре', 'компот',
#       sep='\n\t- ')

num = 10
# Аууууу
# print('А' + 'у' * num) # первый способ
# второй способ
print('А', end='')
for x in range(num):
      print('у', end='')
print()



"""
help(print) - Python Console
print(*args, sep=' ', end='\n', file=None, flush=False)
    Prints the values to a stream, or to sys.stdout by default.
    sep
      string inserted between values, default a space.
    end
      string appended after the last value, default a newline.
    file
      a file-like object (stream); defaults to the current sys.stdout.
    flush
      whether to forcibly flush the stream.
"""