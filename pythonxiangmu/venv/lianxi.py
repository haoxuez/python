def IsPrime(i):
    for a in range(2,i+1):
        if i%a==0:
            return False
        else:
            return True

m=int(input('请输入一个正整数：'))
print(m,'的所有素数约数有：',end='')
for i in range(2,m+1):
    if m%i==0 and IsPrime(i):
        print(i,end=' ')