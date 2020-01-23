import numpy
my_array = numpy.array(list(map(float,input().split())))
print(str(numpy.floor(my_array)).replace('.','. ').replace('[','[ ').replace('. ]','.]'))
print(str(numpy.ceil(my_array)).replace('.','. ').replace('[','[ ').replace('. ]','.]'))
print(str(numpy.rint(my_array)).replace('.','. ').replace('[','[ ').replace('. ]','.]'))

