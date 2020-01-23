import numpy
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(numpy.inner(numpy.array(A),numpy.array(B)));print(numpy.outer(numpy.array(A),numpy.array(B)))
