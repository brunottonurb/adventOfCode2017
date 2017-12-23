a = [0, 2, 7, 0]
b = [11, 11, 13, 7, 0, 15, 5, 5, 4, 4, 1, 1, 7, 1, 15, 11]

def count_cycles(bank = b):
    cycle = 0
    prev_states = set()
    prev_states.add(str(bank))
    while (1):
        cycle += 1
        t = max(bank)
        t_i = bank.index(max(bank))
        bank[t_i] = 0
        while (t > 0):
            t_i += 1
            t_i = t_i % len(bank)
            bank[t_i] += 1
            t -= 1
        if (str(bank) in prev_states):
            return cycle
        prev_states.add(str(bank))

print(count_cycles(b))
