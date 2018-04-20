import numpy
N,M=map(int,input().split())
a = numpy.array([input().split() for _ in range(N)], int)
b = numpy.array([input().split() for _ in range(N)], int)


print(numpy.add(a, b)) 
print(numpy.subtract(a, b))
print(numpy.multiply(a, b))
print(a//b)
print(numpy.mod(a, b))
print(numpy.power(a, b))