import math
import os
import random
import re
import sys




first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []

for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)
string = ''
for row in range(m):
    for col in range(n):
        string += matrix[col][row]
print(re.sub(r'(?<=\w)([#$@%&!\s]+)(?=\w)',' ',string))
