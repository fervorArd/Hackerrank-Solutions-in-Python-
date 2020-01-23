import numpy
matrix = []
for i in range(int(input())):
    matrix.append(list(map(float,(input().split()))))
print(round(numpy.linalg.det(matrix),2))
