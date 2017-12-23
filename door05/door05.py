with open('data') as f:
    j = 0
    l = f.readlines()
    p = 0
    m = len(l)
    li = []
    for i in l:
        li.append(int(i))
    print(li[0])
    while (p >= 0 and p < m):
        t = li[p]
        li[p] += 1
        p += t
        j += 1
        print('.')

print(j)
