import sys


def cubic(b, c, d):
    a = 1
    p = (3 * c - b ** 2) / 3
    q = (2 * b ** 3 - 9 * b * c + 27 * d) / 27
    qb = (p / 3) ** 3 + (q / 2) ** 2
    print('x^3+' + sys.argv[1] + 'x^2+' + sys.argv[2] + 'x+' +
          sys.argv[3])
    if qb > 0:
        print('один вещественный корень и два комплексных')
        alp = (-q / 2 + qb ** (1 / 2)) ** (1 / 3)
        bet = -(q / 2 + qb ** (1 / 2)) ** (1 / 3)
        print('x1 = ' + str(alp + bet - b/3)[:-1])
        print('x2 = ' + str(-0.5 * (alp + bet) + (3**(1 / 2)) * 0.5 *
                            (alp - bet) * (complex(0, 1)) - b/3)[1:-1])
        print('x3 = ' + str(-0.5 * (alp + bet) - (3**(1 / 2)) * 0.5 *
                            (alp - bet) * (complex(0, 1)) - b/3)[1:-1])
    else:
        print('три вещественных корня')
        alp = (-q / 2 + qb ** (1 / 2)) ** (1 / 3)
        bet = (-q / 2 - qb ** (1 / 2)) ** (1 / 3)
        print('x1 = ' + str((alp + bet - b/3))[1:-1])
        print('x2 = ' + str(-0.5 * (alp + bet) + (3**(1/2)) * 0.5 *
                            (alp - bet) * (complex(0, 1)) - b/3)[1:-1])
        print('x3 = ' + str(-0.5 * (alp + bet) - (3**(1/2)) * 0.5 *
                            (alp - bet) * (complex(0, 1)) - b/3)[1:-1])


bc, cc, dc = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
cubic(bc, cc, dc)
