import numpy as np

a = np.zeros([11,11], np.int)

def getHood(x,y):
    return a[x-1,y-1]+a[x,y-1]+a[x-1,y]+a[x-1,y+1]+a[x+1,y-1]+a[x+1,y]+a[x,y+1]+a[x+1,y+1]

def main():
    straight_steps = 1
    x = 5
    y = 5
    a[x,y] = 1
    while (True):
        for i in range(0, straight_steps):
            a[x,y] += getHood(x,y)
            print(a[x,y])
            x += 1
        for i in range(0, straight_steps):
            a[x,y] += getHood(x,y)
            print(a[x,y])
            y += 1
        straight_steps += 1
        for i in range(0, straight_steps):
            a[x,y] += getHood(x,y)
            print(a[x,y])
            x -= 1
        for i in range(0, straight_steps):
            a[x,y] += getHood(x,y)
            print(a[x,y])
            y -= 1
        straight_steps += 1

main()
