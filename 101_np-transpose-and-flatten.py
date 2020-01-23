import numpy
n,m = input().split(); A = []
[A.append(list(map(int,input().split()))) for i in range(int(n))]
print(numpy.transpose(numpy.array(A)))
print(numpy.array(A).flatten())
