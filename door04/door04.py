with open('data') as f:
    s = 0
    phrases = f.readlines()
    for phrase in phrases:
        words = phrase.split()
        if (len(words) == len(set(words))):
            s += 1

print(s)

with open('data') as f:
    s = 0
    phrases = f.readlines()
    valid = 0
    for phrase in phrases:
        phrase = phrase.split()
        if (len(set(map(lambda x: ''.join(sorted(x)), phrase))) == len(phrase)):
            valid += 1
    print(valid)
