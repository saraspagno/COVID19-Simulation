from enum import IntEnum

'''
some global parameters:
    SIZE - the size of the board
    N - number of creatures
    D - number of cells infected at start time
    R - percentage of creatures that can move faster
    X - number of generations until recovery
    P_1, P_2 - probability of infection during high and low infections
    T - threshold value for the change of P as a function of the disease state
'''


class States(IntEnum):
    EMPTY = 0
    HEALTHY = 1
    SICK = 2
    RECOVERED = 3


SIZE = (200, 200)

N = 15000  # number of creatures
D = 0.2  # percentage of infected at start time     0 <= D <= 100
R = 0.4  # percentage of creatures that move faster
REGULAR_MOVEMENT = 1  # the regular movement
FASTER_MOVEMENT = 10  # the faster movement
X = 6  # number of generations until recovery
P_1 = 0.4  # probability of infection during low infections (high)
P_2 = 0.06  # probability of infection during high infections (low)
T = 5  # threshold value for the change of P as a function of the disease state        0 <= T <= 100
