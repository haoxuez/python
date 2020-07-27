print('好友通讯录：')
a={'小明':(1,'广州'),'小红':('002','深圳'),'小王':('003','北京')}
print(a)
x="""""
请输入数字对好友通讯录进行增删改查操作，
请输入数字1进行好友添加，
输入数字2删除好友，
输入数字3修改好友，
输入数字4查询好友，
"""""
print(x)
while True:
    b=int(input())
    if b==1:
        b1=input('请输入好友的姓名，电话，地址：（以逗号隔开）\n')
        b2=tuple(b1.split(',',2))
        a[b2[0]]=b2[1:3]
        print('你要添加的信息是：',b2,'\n',a)
        continue
    elif b==2:
            b3=input('请输入要删除的好友姓名：\n')
            del a[b3]
    elif b==2:
          b3=input('请输入要删除的好友姓名：\n')
          del a[b3]
          print('你要删除的朋友是：',b3,'\n',a)
          continue
    elif b==3:
        b4=input('请输入需要修改的好友姓名，电话，地址：\n')
        b5=tuple(b4.split(',',2))
        a[b5[0]]=b5[1:3]
        print('你要更新的信息是：',b5,'\n',a)
        continue
    elif b==4:
        b6=input('请输入查询的好友的姓名：\n')
        b7=a.get(b6)
        print(b6,'的电话和地址是：',b7)
        continue
    elif b==0:
        print('再见')
        break
    else:
        print('你的输入错误，请重新输入！')
        continue




