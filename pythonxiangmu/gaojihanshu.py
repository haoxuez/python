def nihao(li):
    list=[]
    for i in range(len(li)):
        b=li[i]
        list.append(b**2)
    print('你所需要数的平方为：',list)
x=input('请你输入你要计算的平方的数，可以多个（以空格隔开）：')
list1=x.split(' ')
list2=list(map(int,list1))
nihao(list2)