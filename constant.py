from enum import IntEnum

hello_string = """ 
******* Hello, welcome to this COVID-19 Cellular Automata Simulation! *******
The simulation is run on a 200*200 grid. Before we start, we need some parameters!
"""

enter_parameters = "Press ENTER if you wish to continue with our pre-chosen parameters, or press SPACE+ENTER to choose your own. "
enter_N = "Please type the value of N, the number of creatures. N must be a natural number between 0 and 40,000. "
enter_D = "Please type the value of D, the percentage of infected at start time. D must be a natural number between 0 and 100. "
enter_R = "Please type the value of R, the percentage of creatures that move faster. R must be a natural number between 0 and 100. "
enter_X = "Please type the value of X, the number of generations. X must be a natural number greater than 1. "
enter_P_1 = "Please type the value of P_1, the high probability of infection. P_1 must be between 0 and 1. "
enter_P_2 = "Please type the value of P_2, the low probability of infection. P_1 must be between 0 and 1. "
enter_T = "Please type the value of T, the threshold for changing probability of infection. T must bemust be a natural number between 0 and 100. "

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
