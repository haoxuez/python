class diedq():
    def __iter__(self):
        self.a=1
        return  self
    def __next__(self):
        if self.a>100:
            raise StopIteration
        self.b=self.a
        self.a += 1
        return self.b
my=diedq()
b=[]
for i in my:
    b.append(i)
print('使用迭代对象所求1到100之间的所有整数的和为：',sum(b))

