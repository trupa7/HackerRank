from operator import itemgetter
def person_lister(f):
    def inner(people):
        result=[]
        for i in range(len(people)):
            people[i][2]=int(people[i][2])
        
        my_list=sorted(people, key=itemgetter(2))
        for i in my_list:
            result.append(f(i))     
        return result
    return inner
