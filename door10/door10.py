class node(object):
    def __init__(self, value):
        self.value = int(value)
        self.succ = None
        self.pred = None

    def __str__(self, start = None):
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

def createList(number, succ = None):
    number -= 1
    n = node(number)
    n.succ = succ
    if (succ != None):
        succ.pred = n
    if (number == 0):
        m = n
        while(n.succ != None):
            n = n.succ
        n.succ = m
        m.pred = n
        return m
    return createList(number, n)

n = 256
z = createList(n)
d = [165,1,255,31,87,52,24,113,0,91,148,254,158,2,73,153]

def knot_hash(anchor = createList(5), data = [3,4,1,5], number = 5):
    skipSize = 0
    static = anchor
    print('skipSize = '+  str(skipSize))
    print(static)
    for length in data:
        if (length > number):
            continue
        saveValues = []
        tempPosition = anchor
        for i in range(0, length):
            saveValues.append(tempPosition.value)
            tempPosition = tempPosition.succ
        saveValues.reverse()
        for value in saveValues:
            anchor.value = value
            anchor = anchor.succ
        anchor = anchor.goFurther(skipSize)
        skipSize += 1
        print('---')
        print('skipSize = '+  str(skipSize))
        print(static)

knot_hash(z, d, n)
