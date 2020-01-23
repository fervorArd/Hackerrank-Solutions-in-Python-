import numpy
n,m = input().split();matrix = []
[matrix.append(list(map(int,input().split()))) for i in range(int(n))]
print(numpy.prod(numpy.sum(numpy.array(matrix),axis=0)))
