import random
sum= random.randint(1, 20)
uinput = int(input("请输入一个整数:"))
x= 1
while sum!=  uinput:
    if sum >  uinput:
            print("太小了，请重新输入！")
    elif sum<  uinput:
            print("太大了，请重新输入！")
    x += 1
    uinput= int(input("请输入一个整数："))
print("恭喜您，您猜对了！您一共猜了%d次" % sum)

