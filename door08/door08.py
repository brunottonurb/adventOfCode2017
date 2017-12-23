registers = dict()
with open('data') as f:
    l = f.readlines()
    for s in l:
        s = s.split()

        register = s[0]
        operation = s[1]
        amount = int(s[2])
        register2 = s[4]
        condition = s[5]
        conditor = int(s[6])

        if (not(register in registers)):
            registers[register] = 0
        if (not(register2 in registers)):
            registers[register2] = 0

        if (condition == '!='):
            #print(str(registers[register2])+condition+str(conditor))
            if (registers[register2] != conditor):
                if (operation == 'inc'):
                    registers[register] += amount
                elif (operation == 'dec'):
                    registers[register] -= amount

        elif (condition == '>'):
            #print(str(registers[register2])+condition+str(conditor))
            if (registers[register2] > conditor):
                if (operation == 'inc'):
                    registers[register] += amount
                elif (operation == 'dec'):
                    registers[register] -= amount

        elif (condition == '<'):
            #print(str(registers[register2])+condition+str(conditor))
            if (registers[register2] < conditor):
                if (operation == 'inc'):
                    registers[register] += amount
                elif (operation == 'dec'):
                    registers[register] -= amount

        elif (condition == '<='):
            #print(str(registers[register2])+condition+str(conditor))
            if (registers[register2] <= conditor):
                if (operation == 'inc'):
                    registers[register] += amount
                elif (operation == 'dec'):
                    registers[register] -= amount

        elif (condition == '>='):
            #print(str(registers[register2])+condition+str(conditor))
            if (registers[register2] >= conditor):
                if (operation == 'inc'):
                    registers[register] += amount
                elif (operation == 'dec'):
                    registers[register] -= amount

        elif (condition == '=='):
            #print(str(registers[register2])+condition+str(conditor)+"="+str(registers[register2] == conditor))
            if (registers[register2] == conditor):
                if (operation == 'inc'):
                    registers[register] += amount
                elif (operation == 'dec'):
                    registers[register] -= amount

        else:
            print(condition)

    print(max(zip(registers.values(), registers.keys())))
