from time import sleep

def get_groups(data, c):
    group = set(c)
    with open(data) as f:
        l = f.readlines()
        lines = list(map(lambda x: x.replace('<->','').replace(',','').split(), l))
        while True:
            old_len = len(group)
            for line in lines:
                for item in line:
                    if item in group:
                        for item in line:
                            group.add(item)
                        break
            if (old_len == len(group)):
                break
    return group

g = get_groups('data', '0')
print(len(g))
