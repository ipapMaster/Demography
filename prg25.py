# Операции над множествами
a = {1, 2, 3, 4}
b = {2, 3, 5, 7, 11}

# объединение множеств (union)
# result = a.union(b)
# result = a | b  # | - "ИЛИ"

# пересечение множеств
# result = a.intersection(b)
# result = a & b  # & - "И"

# разность множеств
# result = a.difference(b)
result = a - b

# симметричная разность
# result = a.symmetric_difference(b)
result = a ^ b

print(result)
