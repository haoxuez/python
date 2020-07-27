def func1(li):
    if len(li) % 2 == 0:
         d=li[len(li) // 2 - 1]+li[len(li) // 2]
         end=d/2
         print(end)
    elif len(li) % 2 != 0:
        print(li[len(li) // 2])
x = input("input number:")
list11=x.split(' ')
list11=list(map(int,list11))
list1 = sorted(list11)
print(list1)
func1(list1)
