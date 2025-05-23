# Даны две строки строчных латинских символов: строка J и строка S.
# Символы, входящие в строку J, — «драгоценности», входящие в строку S — «камни».
# Нужно определить, какое количество символов из S одновременно являются «драгоценностями»
# Проще говоря, нужно проверить, какое количество символов из S входит в J.

# Это разминочная задача, к которой мы размещаем готовые решения.
# Она очень простая и нужна для того, чтобы вы могли познакомиться
# с нашей автоматической системой проверки решений.
# Ввод и вывод осуществляется через файлы, либо через стандартные потоки ввода-вывода, как вам удобнее.

# Формат ввода
# На двух первых строках входного файла содержатся две строки
# строчных латинских символов: строка J и строка S. Длина каждой не превосходит 100 символов.
# Формат вывода
# Выходной файл должен содержать единственное число — количество камней, являющихся драгоценностями.

# import sys

# J = sys.stdin.readline()
# S = sys.stdin.readline()

# count_jewels = 0

# for c in S:
#     if c in J:
#         count_jewels += 1

# print(count_jewels)

# # or

jewels = input().strip()
stones = input().strip()

jewel_set = set(jewels)
count = sum(ch in jewel_set for ch in stones)

# count = 0
# for char in stones:
#     if char in jewel_set:
#         count += 1

print(count)


# # с тестами
# def count_jewels(jewels: str, stones: str) -> int:
#     jewel_set = set(jewels)
#     return sum(ch in jewel_set for ch in stones)


# assert count_jewels("a", "aAa") == 2
# assert count_jewels("ab", "aabbccd") == 4
# assert count_jewels("", "abc") == 0
# assert count_jewels("abc", "") == 0

# print("✓ All tests passed")
