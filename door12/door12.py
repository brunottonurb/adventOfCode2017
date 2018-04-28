from copy import deepcopy

def get_groups(data):
    groups = []
    with open(data) as f:
        l = f.readlines()
        groups = list(map(lambda x: set(x.replace('<->','').replace(',','').split()), l))
        c = 0
        while c < 100:
            newGroups = []
            for group in groups:
                for otherGroup in groups:
                    if (len(group & otherGroup) > 0):
                        newGroups.append(group | otherGroup)
            if (newGroups == groups):
                break
            groups = newGroups
            print(c)
            c += 1


    return groups

g = get_groups('data')
for j in g:
    if '0' in j:
        print(len(j))
print(len(g))
