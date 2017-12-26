def magic_score(data):
    l = len(data)

    group_value = 0
    total_score = 0
    is_garbage = False

    garbage_counter = 0

    i = 0
    while (i < l):

        # do the garbage counting
        if (is_garbage == True):
            if (data[i] != '!' and data[i] != '>'):
                garbage_counter += 1

        if (data[i] == '!'):
            i += 2
            continue
        elif (data[i] == '<'):
            is_garbage = True
            i += 1
            continue
        elif (data[i] == '>'):
            is_garbage = False
            i += 1
            continue
        elif (not(is_garbage)):
            if (data[i] == '{'):
                group_value += 1
                i += 1
                continue
            elif (data[i] == '}'):
                total_score += group_value
                group_value -= 1
                i += 1
                continue
        i += 1
    print(garbage_counter)
    return total_score


def main():
    with open('data') as f:
        data = f.readline()
        print(magic_score(data))

main()
