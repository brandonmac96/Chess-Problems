from random import randint
import numpy as np


def random_position():
    pos = 64*["*"]
    for i in range(4):
        if randint(0, 3) > 0:
            pos[randint(8, 15)] = "p"
    for i in range(1):
        if randint(0, 3) > 1:
            pos[randint(16, 23)] = "p"
    for i in range(1):
        if randint(0, 3) > 1:
            pos[randint(24, 31)] = "p"
    for i in range(1):
        if randint(0, 3) > 1:
            pos[randint(32, 39)] = "p"
    for i in range(1):
        if randint(0, 3) > 1:
            pos[randint(48, 55)] = "p"

    for i in range(3):
        if randint(0, 3) > 0:
            pos[randint(48, 55)] = "P"
    for i in range(3):
        if randint(0, 3) > 1:
            pos[randint(40, 47)] = "P"
    for i in range(1):
        if randint(0, 3) > 1:
            pos[randint(16, 23)] = "P"
    for i in range(1):
        if randint(0, 3) > 1:
            pos[randint(8, 15)] = "P"

    if randint(0, 2) > 0:
        if randint(0, 2) > 0:
            pos[1] = "k"
        else:
            pos[6] = "k"

    if randint(0, 2) > 0:
        pos[randint(16, 31)] = "k"


    if randint(0, 2) > 0:
        if randint(0, 2) > 0:
            pos[57] = "K"
        else:
            pos[62] = "K"

    if randint(0, 2) > 0:
        pos[randint(32, 47)] = "K"


    if randint(0, 2) > 0:
        pos[randint(32, 47)] = "b"

    if randint(0, 2) > 0:
        pos[randint(16, 31)] = "B"

    if randint(0, 3) > 1:
        pos[0] = "r"
    if randint(0, 3) > 1:
        pos[7] = "r"

    if randint(0, 3) > 1:
        pos[56] = "R"
    if randint(0, 3) > 1:
        pos[63] = "R"

    if randint(0, 3) > 1:
        pos[randint(16, 47)] = "q"
    if randint(0, 3) > 1:
        pos[randint(16, 47)] = "Q"

    pos[randint(2, 5)] = "x"
    pos[randint(58, 61)] = "X"

    return "".join(pos)


def check_tester(in_check, pretty_print):
    test_pos = ["r***rx**p**K*pppBp****q**Q*********P******P**********PPP***R**X*",  # knight attack True
                "R***rx**R***bppp*p****q**********B*P******P**Q*******PPP***R**X*",  # all blocked False
                "r*x*r***ppp**ppp*k***********BBq*********Q******PP*R*PPP****X***",  # bishop attack True
                "r*x*r***ppp***pp*k**p********BB**********Q******PP*R*PPP****X***",  # defending pawn False
                "r***r***ppx***pp*kp**p********k******Q**********PP*R*PPP****X***",  # queen attack True
                "r***r***pp******xk*R*p********kK*****Q**********************X***",  # deceptive False
                "r***r***pp******x**R*p**k*****bK*****Q***********************X**",  # rook attacking True
                "r***rx****q**ppp*p***************KP*******P**Q*****R*PPP****X***",  # all good False
                "r***r***pp******xp***p**kP****bK****RQ***********************X**",  # pawn attacking True
                "r***r****p*******p*x*K**k***q*b*****R**********Q***P******P**X**"]  # all good False

    count = 0
    for i in range(10):
        pretty_print(test_pos[i])
        actual_check = i % 2 == 0
        reported_check = in_check(test_pos[i])
        print("The white king is in check: ", actual_check)
        print("Your method reports: ", reported_check)

        if reported_check == actual_check:
            print("Your answer is CORRECT! \n")
            count = count + 1
        else:
            print("Your answer is NOT correct! \n")

    print("You answered correctly {}% of the tests.".format(count*10))


def random_position2():
    pos = 64*["*"]

    if randint(0, 2) > 0:
        P = 5
        p = 0
    else:
        P = 0
        p = 5

    for i in range(4):
        if randint(0, 5) > p:
            pos[randint(8, 15)] = "p"
    for i in range(1):
        if randint(0, 5) > p:
            pos[randint(16, 23)] = "p"
    for i in range(1):
        if randint(0, 5) > p:
            pos[randint(24, 31)] = "p"
    for i in range(1):
        if randint(0, 5) > p:
            pos[randint(32, 39)] = "p"
    for i in range(1):
        if randint(0, 5) > p:
            pos[randint(48, 55)] = "p"

    for i in range(3):
        if randint(0, 5) > P:
            pos[randint(48, 55)] = "P"
    for i in range(3):
        if randint(0, 5) > P:
            pos[randint(40, 47)] = "P"
    for i in range(1):
        if randint(0, 5) > P:
            pos[randint(16, 23)] = "P"
    for i in range(1):
        if randint(0, 5) > P:
            pos[randint(8, 15)] = "P"

    if randint(0, 5) > p:
        if randint(0, 5) > p:
            pos[1] = "k"
        else:
            pos[6] = "k"

    if randint(0, 5) > p:
        pos[randint(16, 31)] = "k"


    if randint(0, 5) > P:
        if randint(0, 5) > P:
            pos[57] = "K"
        else:
            pos[62] = "K"

    if randint(0, 5) > P:
        pos[randint(32, 47)] = "K"


    if randint(0, 5) > p:
        pos[randint(32, 47)] = "b"

    if randint(0, 5) > P:
        pos[randint(16, 31)] = "B"

    if randint(0, 5) > p:
        pos[0] = "r"
    if randint(0, 5) > p:
        pos[7] = "r"

    if randint(0, 5) > P:
        pos[56] = "R"
    if randint(0, 5) > P:
        pos[63] = "R"

    if randint(0, 5) > p:
        pos[randint(16, 47)] = "q"
    if randint(0, 5) > P:
        pos[randint(16, 47)] = "Q"

    pos[randint(2, 5)] = "x"
    pos[randint(58, 61)] = "X"

    return "".join(pos)


def oracle(pos_array):
    unique, counts = np.unique(pos_array, return_counts=True)
    dict_piece = dict(zip(unique, counts))
    value = np.sum(pos_array)+np.sum(pos_array[2:6, 2:6])

    for k in dict_piece:
        if k != 0 and dict_piece[k] > 1:
            value = value + k * abs(k) * dict_piece[k]

    if value > 20:
        return 1
    if value < -20:
        return -1
    return 0

