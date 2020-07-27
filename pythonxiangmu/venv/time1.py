class Time:
    hour,minute,second=0,0,0
    isCorrect=False

    def sethour(self):
        hr=int(input('请输入小时数：'))
        if 0<hr<24:
            self.hour=hr
            self.isCorrect=True
        else:
            print('你输入的小时数不在0~24之间，请重新输入！')
            isCorrect=False

    def setMinute(self):
        m=int(input('请输入分钟数：'))
        if 0<m<60:
            self.minute=m
            self.isCorrect=True
        else:
            print('你输入的小时数不在0~60之间，请重新输入！')
            isCorrect=False

    def setSecond(self):
            s = int(input('请输入秒数：'))
            if 0 < s < 60:
                    self.second =s
                    self.isCorrect = True
            else:
              print('你输入的秒数不在0~60之间，请重新输入！')
            isCorrect =False

    def Showtime(self):
              print('你设置的时间为%d:%d:%d'%(self.hour,self.minute,self.second))
class Database(Time):
    year,month,day=0,0,0
    def setYear(self):
        a=int(input('请输入年份数：'))
        if  1900<=a<=2000:
            self.year=a
            self.isCorrect=True
        else:
            print('你输入的年数不在之间，请重新输入！')
            self.isCorrect=False

    def setMonth(self):
        b=int(input("请输入月份数："))
        if 1<=b<=12:
            self.month=b
            self.isCorrect=True
        else:
            print('你输入的月数不在0-12之间，请重新输入！')
            self.isCorrect=False

    def setDay(self):
        c= int(input("请输入日期数："))
        if 1 <= c <= 30:
            self.day = c
            self.isCorrect = True
        else:
            print('你输入的日期数不在1-30之间，请重新输入！')
            self.isCorrect = False
    def Showtime(self):
        print('你设置的日期为%d-%d-%d  %d:%d:%d' % (self.year,self.month,self.day,self.hour, self.minute, self.second))
mytime=Database()
mytime.setYear()
mytime.setMonth()
mytime.setDay()
mytime.sethour()
mytime.setMinute()
mytime.setSecond()
mytime.Showtime()






