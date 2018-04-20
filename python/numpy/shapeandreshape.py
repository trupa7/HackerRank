import numpy

change_array = numpy.array([int(n) for n in input().split(" ")])
change_array.shape = (3, 3)
print(change_array)