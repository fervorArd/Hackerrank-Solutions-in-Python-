import numpy
N = int(input());A = [];B = []
[A.append(list(map(int,input().split()))) for i in range(N)]
[B.append(list(map(int,input().split()))) for i in range(N)]
print(numpy.dot(numpy.array(A),numpy.array(B)))
