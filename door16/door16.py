class node(object):
    def __init__(self, value):
        self.value = value
        self.succ = None
        self.pred = None

    def __str__(self, start = None):
        if (self.value==start):
            return ''
        if (start == None):
            start = self.value
        return self.value+'\t'+self.succ.__str__(start)

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

def create_line(index = 16, word='abcdefghijklmnop', succ = None):
    index -= 1
    n = node(word[index])
    n.succ = succ
    if (succ != None):
        succ.pred = n
    if (index == 0):
        m = n
        while(n.succ != None):
            n = n.succ
        n.succ = m
        m.pred = n
        return m
    return create_line(index, word, succ)

anchor = create_line()
print(anchor.__str__())
