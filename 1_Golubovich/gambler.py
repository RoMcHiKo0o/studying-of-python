import sys
import random


def gambler(st, go, tr):
    i = 1
    for i in range(tr + 1):
        st += random.choice([-1, 1])
        if st == 0:
            return 0
        if st == go:
            return 0


def gambler2(st, go, tr):
    i = 1
    for i in range(tr + 1):
        st += random.choice([-1, 1])
        if st == 0 or st == go:
            return i
    return 0


def gambler3(st, go, tr):
    s = st
    i = 1
    for i in range(tr + 1):
        st += random.choice([-1, 1])
        if st > s:
            s = st
        if st == 0 or st == go:
            break
    return s


stake, goal, trials, lives = int(sys.argv[1]), int(sys.argv[2]), \
                             int(sys.argv[3]), int(sys.argv[4])
# пункт 1
'''win = 0
loss = 0
for i in range(lives):
    res = gambler(stake, goal, trials)
    if res == 1:
        win += 1
    if res == 0:
        loss += 1
print('выигрыш:', win * 100 / lives, 'процентов')
print('проигрыш:', loss * 100 / lives, 'процентов')'''
# пункт 2
'''s = 0
for i in range(lives):
    res = gambler2(stake, goal, trials)
    s += res
    # print(res, 'из', trials, 'попыток')
s = s / lives / trials
print(s * 100, 'процентов')
'''
# пункт 3
s = 0
for i in range(lives):
    s += gambler3(stake, goal, trials)
s = s / goal / lives
print(s * 100, 'процентов')
'''
все проверялось при стартовом стеке 100 и при цели в 1000.

пункт 1: выигрыш при 10 миллионах попыток примерно 10 процентов,
 проигрыш примерно 90.
 
 пункт 2: я считал процент попыток которые нужны,
  чтоб дойти до 0 или цели
  10кк шагов = 1 процент
  1кк шагов = 8 процентов
  100к шагов = 16.5-17 процентов
  10к шагов = 16.0-16.5 процентов
  1к шагов = 0.15 процентов
  
  пункт 3: 10кк шагов = 33.3 процент от цели
  1кк шагов = около 30 процентов от цели
  100к шагов = около 27 процентов от цели
  10к шагов = около 17.5 процентов от цели
  1к шагов = 12.5 процентов от цели'''
