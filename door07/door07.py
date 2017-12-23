class node(object):
    def __init__(self, value):
        self.value = value
        self.children = []
        self.weight = 0

    def __str__(self, level=0):
        ret = "  |  "*level+repr(self.value)+":"+repr(self.weight)+"\n"
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
        return None

def door07(data):
    root = node('bqyqwn')
    root.weight = 68
    for x in ['wscqe', 'cwxspl', 'syogw', 'xnxudsh']:
        root.children.append(node(x))

    with open(data) as f:
        l = f.readlines()
        l = list(l)
        # = []
        while (len(l) > 0):
            for st in l:
                s = st.split()
                name = s[0]; #print(name)
                weight = int(s[1][1:-1]); #print(weight)
                children = []
                if (len(s) > 2):
                    #children = s[3:]
                    for child in s[3:-1]:
                        children.append(child[:-1])
                    children.append(s[-1])
                # print(children)
                location = root.search(name)
                if (location):
                    for child in children:
                        location.children.append(node(child))
                    location.weight = weight
                    #print('inserted above')
                    l.remove(st)
                elif (root.value in children):
                    #print("inserted as root")
                    new = node(name)
                    for child in children:
                        new.children.append(node(child))
                    location = new.search(root.value)
                    location.children = root.children
                    root = new
                    l.remove(st)

        print(root)
        #print(later)

door07('data')

def comment2():
    root = node('bqyqwn')
    root.weight = 68
    for x in ['wscqe', 'cwxspl', 'syogw', 'xnxudsh']:
        root.children.append(node(x))
    #door07('data')
    with open('test') as f:
        l = f.readlines()
        for s in l:
            s = s.split()
            name = s[0]; #print(name)
            weight = int(s[1][1:-1]); #print(weight)
            children = []
            if (len(s) > 2):
                #children = s[3:]
                for child in s[3:-1]:
                    children.append(child[:-1])
                children.append(s[-1])
            print(children)
            #print(children.index(root.value))
            print(children[0])
            print(root.value)
            print(root.value == children[0])


#"bqyqwn (68) -> wscqe, cwxspl, syogw, xnxudsh"
def comment():
    root = node('1')
    n = node('2')
    m = node('3')
    o = node('4')
    p = node('5')

    o.weight = 2

    o.children = [p]
    n.children = [o,m]
    root.children = [n]

    new = node('here')
    new.children.append(root)
    root = new
    print(root)
