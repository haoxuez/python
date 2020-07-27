with open(r'D:\py\my_txt.txt','w')as f:
    f.write(str('我在学习Python的文件操作方法。\n'))
    f.write(str('文本文件的写入方法.\n'))
    f.write('文本文件的读取方法。')
with open(r'D:\py\my_txt.txt','r')as y:
    for line in y:
        print(line.rstrip())




