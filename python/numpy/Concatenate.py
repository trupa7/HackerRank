import numpy
n=list(map(int,input().split(" ")))
my_list=[]
for _ in range(n[0]+n[1]):
    my_list.append(list(map(int,input().split(" "))))
my_list1=numpy.array(my_list)
print(my_list1)