with open('data') as f:
    s = 0
    phrases = f.readlines()
    for phrase in phrases:
        words = phrase.split()
        if (len(words) == len(set(words))):
            s += 1

print(s)
