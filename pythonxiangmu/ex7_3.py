import csv
with open(r'd:\py\instance.csv','w'as f:
    w=csv.writer(f)
    w.writerows([['class','name','course','score'],['19大数据3','li','python','90'],
                ['19大数据3','zhou','python','69'],['19大数据3','jun','python','75'],['19大数据3','ren','python','63']])
with open(r'd:\py\instance.csv','r',)as rd:
    read=csv.reader(rd)
    for i in read:
        print(i)