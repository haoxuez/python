def Func(s):
    m=min(s)
    list1=[m,]
    j=0
    for k in s:
        if k==m:
            list1.append(j)
        j=j+1
    return  tuple(list1)
from random import  randint
x=[randint(1,20) for i in range(20)]
print(x)
print(Func(x))