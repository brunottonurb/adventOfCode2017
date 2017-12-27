def calc_severity(data):
    with open(data) as f:
        l = f.readlines()
        layers = {}
        backup = {}
        for i in l:
            i = i.split()
            layers[int(i[0].strip(':'))] = 2 * int(i[1]) - 2
            backup[int(i[0].strip(':'))] = int(i[1])

        severity = 0
        for pico in range(0, 100):
            if (pico in layers):
                print(str(pico)+':'+str(pico % layers[pico])+'/'+str(layers[pico]))
                if (pico % layers[pico] == 0):
                    severity += pico * backup[pico]
        print(severity)

calc_severity('data')

print
