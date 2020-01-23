import numpy
n,m = list(map(int,input().split()))
print(str(numpy.eye(n,m,k=0)).replace('[','[ ').replace('[ [ ','[[ ').replace('.','. ').replace('. ]','.]'))
