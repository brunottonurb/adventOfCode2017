def manhattan_distance(number = 277678):
    x = 1
    straight_steps = 1
    horizontal_distance = 0
    vertical_distance = 0

    if (number == 1):
        return 0

    while (1):
        # number of steps before turn increses with every second turn
        # 1 1 2 2 3 3 4 4 5 5


        # do horizontal
        for i in range(1, straight_steps+1):
            if (i <= (straight_steps / 2)):
                horizontal_distance -= 1
            else:
                horizontal_distance += 1
            x += 1
            if (x == number):
                return horizontal_distance + vertical_distance

        # do vertical
        for i in range(1, straight_steps+1):
            if (i <= (straight_steps / 2)):
                vertical_distance -= 1
            else:
                vertical_distance += 1
            x += 1
            if (x == number):
                return horizontal_distance + vertical_distance

        # increase straight_steps
        straight_steps += 1

print(manhattan_distance())
