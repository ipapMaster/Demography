# Функции-антонимы chr и ord
# ASCII (256) - 8 бит, т.е. 1 байт (2^8)
# Unicode (65536) - 16 бит т.е. 2 байта (2 ^ 16)
import string as s

# print(ord('a'))
# print(chr(97))
temp = s.digits + s.ascii_lowercase + s.ascii_uppercase
m_set = set(temp) - {'l', 'O', 'I', '1', '0'}
print(m_set)
st = '«ПРИВЕТ»'
print(ord('«'))

print(f'{chr(171)}ПРИВЕТ{chr(187)}')
print(chr(10000))
print('75' + chr(176) + 'C')
print(f'75{chr(176)}C')
print('75\xB0C')  # hex ASCII
print('\u2710')  # Unicode

# \xB0 = chr(176)
