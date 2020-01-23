import numpy
n,m = list(map(int,input().split()));a = [];b = []
[a.append(list(map(int,input().split()))) for i in range(n)]
[b.append(list(map(int,input().split()))) for i in range(n)]
a = numpy.array(a)
b = numpy.array(b)
print(*map(str,[a+b,a-b,a*b,a//b,a%b,a**b]),sep='\n')
