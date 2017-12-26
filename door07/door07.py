class node(object):
    def __init__(self, value):
        self.value = value
        self.children = []
        self.weight = 0

    def __str__(self, level=0):
        intend = ''
        if level>0:
            intend = "  |--"
        ret = "  |  "*(level-1)+intend+repr(self.value)+":"+str(self.getWeight())+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return '<tree node representation>'

    def search(self, value):
        if (self.value == value):
            return self
        c = list(filter(lambda x: x.search(value), self.children))
        if (len(c) > 0):
            return c[0].search(value)

    def getWeight(self):
        w = self.weight
        for child in self.children:
            w += child.getWeight()
        return w


def door07(data):
    root = node('bqyqwn')
    #root = node('fwft')
    root.weight = 68
    #root.weight = 72
    for x in ['wscqe', 'cwxspl', 'syogw', 'xnxudsh']:
    #for x in ['ktlj', 'cntj', 'xhth']:
        root.children.append(node(x))

    with open(data) as f:
        l = f.readlines()
        l = list(l)
        while (len(l) > 0):
            for st in l:
                s = st.split()
                name = s[0]; #print(name)
                weight = int(s[1][1:-1]); #print(weight)
                children = []
                if (len(s) > 2):
                    for child in s[3:-1]:
                        children.append(child[:-1])
                    children.append(s[-1])
                location = root.search(name)
                if (location):
                    for child in children:
                        location.children.append(node(child))
                    location.weight = weight
                    l.remove(st)
                elif (root.value in children):
                    new = node(name)
                    new.weight = weight
                    for child in children:
                        new.children.append(node(child))
                    location = new.search(root.value)
                    location.weight = root.weight
                    location.children = root.children
                    root = new
                    l.remove(st)

        return root

def door072(o):
    #recursive baby! yeah baby!
    if (len(o.children) > 0):
        if (len(set(map(lambda x: x.getWeight(), o.children))) > 1):
            print(o.value)
            print('\n--------------------\n')
        for child in o.children:
            door072(child)

r = door07('data')
#r = door07('test')
print(r)
door072(r)

n = r.search('gozhrsf')
print(n.value+':\t'+str(n.weight))
print(n)
for n in n.children:
    print(n.value+':\t'+str(n.getWeight()))

print(762-5)
