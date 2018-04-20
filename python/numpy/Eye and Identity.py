import numpy
n=list(map(int,input().split(" ")))
numpy.set_printoptions(sign=' ')
print (numpy.eye(n[0], n[1], k = 0))