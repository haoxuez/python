print('abcdefghijklmnopqrstuvwxyz')
s=input('请输入你的明文：')
for i in s:
    if 'a'<=i<='u':
        x=chr(ord(i)+5)
    elif 'v'<=i<='z':
        x=chr(ord(i) -21)
    else:
        x=i

    print(x,end='')
