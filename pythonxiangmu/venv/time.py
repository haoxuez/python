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
mytime = Time()
mytime.sethour()
mytime.setMinute()
mytime.setSecond()
mytime.Showtime()
