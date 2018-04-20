import numpy
N,M=map(int,input().split())
my_list=[]
for i in range(N):
    my_list.append(list(map(int,input().split())))
my_array = numpy.array(my_list)

print(numpy.prod(numpy.sum(my_array, axis=0)))