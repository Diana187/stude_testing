# Формат ввода
# Первая строка входа содержит числа A и B ( − 2 ⋅ 109 ≤ A,B ≤ 2 ⋅ 109) разделенные пробелом
# Формат вывода
# В единственной строке выхода выведите сумму чисел A+B

import sys

line = sys.stdin.readline()

a, b = map(int, line.split())
sys.stdout.write(f"{a + b}\n")

# or
a, b = map(int, input().split())

print(a + b)
