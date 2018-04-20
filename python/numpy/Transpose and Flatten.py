iimport numpy
a=list(map(int,input().split(" ")))
a_list=[]
for i in range(int(a[0])):
    a_list.append(list(map(int,input().split(" "))))
my_array = numpy.array(a_list)
print(numpy.transpose(a_list))
print(my_array.flatten())