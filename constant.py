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

N = 10000  # number of creatures
D = 1000  # number of cells infected at start time
R = 0.1  # percentage of creatures that move faster
REGULAR_MOVEMENT = 1  # the regular movement
FASTER_MOVEMENT = 10  # the faster movement
X = 10  # number of generations until recovery
P_1 = 0.9  # probability of infection during low infections
P_2 = 0.9  # probability of infection during high infections
T = 0.6  # threshold value for the change of P as a function of the disease state
