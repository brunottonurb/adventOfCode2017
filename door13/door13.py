def calc_severity(data, delay):
    with open(data) as f:
        l = f.readlines()
        layers = {}
        backup = {}
        for i in l:
            i = i.split()
            layers[int(i[0].strip(':'))] = 2 * int(i[1]) - 2
            backup[int(i[0].strip(':'))] = int(i[1])

        severity = 0
        pico = 0
        caught = False
        while True:
            if (pico in layers):
                # print(str(pico+delay)+':'+str((pico+delay) % layers[pico])+'/'+str(backup[pico]))
                if ((pico+delay) % layers[pico] == 0):
                    severity += pico * backup[pico]
                    caught = True
            if (pico >= max(layers.keys())):
                break
            pico += 1
        return (caught, severity)

#calc_severity('data', 0)

delay = 0
while True:
    caught, sev = calc_severity('data', delay)
    print('delay = '+str(delay)+'\tseverity = '+str(sev))
    if not caught:
        break
    delay += 1

print(delay)
