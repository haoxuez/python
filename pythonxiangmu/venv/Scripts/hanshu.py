def nihao(n):
    if n <= 1:
        return 1
    else:
        return nihao(n - 1) + nihao(n - 2)
a=int(input('请你输入需要求斐波那契数列的第N项：'))
if a<0:
    print('你输入的数据有误请重新输入：')
else:
    print('%s',a,nihao(a))

