import numpy
my_array = numpy.array(list(map(float,input().split())))
numpy.set_printoptions(sign=" ")
print (numpy.floor(my_array), numpy.ceil(my_array)  , numpy.rint(my_array),sep='\n') 