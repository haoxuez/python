cost=160
qt=int(input('请输入你要买的数量：'))
if 1<=qt<=4:
    sum=cost*0.9*qt
elif 5<=qt<=9:
    sum = cost * 0.8 * qt
else:
    sum = cost * 0.7 * qt
print(sum)
