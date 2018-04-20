import numpy
N,M=map(int,input().split())
a_list=[]
for i in range(N):
    a_list.append(list(map(int,input().split())))
my_array = numpy.array(a_list)

print (numpy.max(numpy.min(my_array, axis = 1)  ) )