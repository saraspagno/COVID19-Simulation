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

N = 8000  # number of creatures
D = 0.1  # percentage of infected at start time     0 <= D <= 100
R = 10  # percentage of creatures that move faster 0 <= R <= 100
REGULAR_MOVEMENT = 1  # the regular movement
FASTER_MOVEMENT = 10  # the faster movement
X = 8  # number of generations until recovery
P_1 = 0.2  # probability of infection during low infections (high)
P_2 = 0.1  # probability of infection during high infections (low)
P = P_1  # standard probability
T = 8  # threshold value for the change of P as a function of the disease state        0 <= T <= 100
C = T * 0.6  # threshold change

these_parameters = f"""
Done! These are the parameters for the simulation: 
N = {N}
D = {D}
R = {R}
X = {X}
P_1 = {P_1}
P_2 = {P_2}
T = {T}

Starting the simulation now.
"""
