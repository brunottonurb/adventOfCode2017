data = 376

class node(object):
    def __init__(self, value):
        self.value = int(value)
        self.succ = None
        self.pred = None

    def __str__(self, start = None):
        print(start)
        if (self.value==start):
            return ''
        if (start == None):
            start = self.value
        return str(self.value)+'\t'+self.succ.__str__(start)

    def __repr__(self):
        return '<linkedlist node representation>'

    def find(self, number, start = None):
        if (self.value == number):
            return self
        elif (self.value == start):
            return None
        if (start == None):
            start = self.value
        return self.succ.find(number, start)

    def goFurther(self, number):
        if (number <= 0):
            return self
        return self.succ.goFurther(number -1)

def spinLock(step, number = 2018):
    buff = node(0)
    buff.succ = buff
    for i in range(1, number):
        for j in range(step):
            buff = buff.succ
        new = node(i)
        temp = buff.succ
        buff.succ = new
        new.succ = temp
        buff = buff.succ
    print(buff.succ.value)

spinLock(data)
























    #
