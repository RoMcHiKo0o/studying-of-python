import sys
import random


def monty(change):
    prize = random.choice([0, 1, 2])
    mychoice = random.choice([0, 1, 2])
    if mychoice == prize:
        if change == 1:
            return 0
        else:
            return 1
    else:
        if change == 1:
            return 1
        else:
            return 0


def montyhard(doors, prizes, showndoors, change):
    prize = random.choice(range(doors))
    choice = random.choice(range(doors))
    if 1 + prizes + showndoors <= doors:
        if choice == prize:
            if change == 1:
                return random.choices([1, 0],
                                      weights=[prizes-1, doors - prizes - showndoors])[0]
            else:
                return 1
        else:
            if change == 1:
                return random.choices([1, 0],
                                      weights=[prizes, doors - 1 - prizes - showndoors])[0]
            else:
                return 0

    else:
        print('smth wrong')


# первый пункт
'''tries = int(sys.argv[1])
win = 0
for i in range(tries):
    if monty(1):
        win += 1
print('выигрыш при смене:', win * 100 / tries, 'процентов')
i = 0
win = 0
for i in range(tries):
    if monty(0):
        win += 1
print('выигрыш без смены:', win * 100 / tries, 'процентов')'''
# второй пункт
doors, prizes, showndoors, tries = int(sys.argv[1]),\
                                   int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
win = 0
for i in range(tries):
    if montyhard(doors, prizes, showndoors, 1):
        win += 1
print('выигрыш при смене:', win * 100 / tries, 'процентов')
i = 0
win = 0
for i in range(tries):
    if montyhard(doors, prizes, showndoors, 0):
        win += 1
print('выигрыш без смены:', win * 100 / tries, 'процентов')
