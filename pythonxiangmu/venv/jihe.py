num1=int(input('请输入你的需要运算的第一个数：'))
num2=int(input('请输入你需要运算的第二个数'))
s1=[i for i in range(1,num1+1) if num1%i==0]
s2=[i for i in range(1,num2+1) if num2%i==0]
print('%s的约数集为：'%(num1),s1)
print('%s的约数集为：'%(num2),s2)
s4=set(s1)
s5=set(s2)
print('公约数值为：',s4&s5)
s6=max(s4&s5)
print('最大的公约数为：',s6)
s7=min(s4&s5)
print('最小公倍数为：',s7)