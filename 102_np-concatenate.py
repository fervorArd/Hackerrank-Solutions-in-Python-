import numpy
array_1 = []
array_2 = []
n,m,p = input().split()
[array_1.append(list(map(int,input().split()))) for i in range(int(n))]
[array_2.append(list(map(int,input().split()))) for i in range(int(m))]
print(str(numpy.array(array_1 + array_2)))
#print(str(numpy.concatenate((numpy.array(array_1),numpy.array(array_2)))))
