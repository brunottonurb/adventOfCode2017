with open('data') as f:
    j = 0
    lines = f.readlines()
    lines = list(map(lambda x: int(x), lines))
    p = 0
    while (p >= 0 and p < len(lines)):
        t = lines[p]
        lines[p] += 1
        p += t
        j += 1
        print('.')

print(j)


with open('data') as f:
    j = 0
    lines = f.readlines()
    lines = list(map(lambda x: int(x), lines))
    p = 0
    while (p >= 0 and p < len(lines)):
        t = lines[p]
        if (t >= 3):
            lines[p] -= 1
        else:
            lines[p] += 1
        p += t
        j += 1

print(j)
