def wrapper(f):
    def fun(l):
        my_list=[]
        for i in range(len(l)):
            p=l[i]
            my_list.append(p[-10:])
        my_list.sort()
        for i in range(len(my_list)):
            q=my_list[i]
            print('+91 '+q[-10:-5]+' '+q[-5:])
    return fun