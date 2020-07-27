class Triangle:
    a,b,c=0,0,0
    isCorrect=False

    def iscorrect(self):
        sum1= input('请输入第三条边边长')
        sum2= input('请输入第一条边边长')
        sum3= input('请输入第二条边边长')
        if sum1 + sum2 > sum3 and sum1+ sum3 > sum2 and sum2 + sum3 > sum1:
            isCorrect = True
            self.a= sum1
            self.b= sum2
            self.c=sum3
        else:
        print('你输入的三边不能构成三角形，请重新输入！')
            isCorrect=False

    def printZC(self):
        l=(a+b+c)//2

