from enum import Enum

class States(Enum):
    EMPTY = 0
    HEALTHY = 1
    SICK = 2
    RECOVERED = 3

SIZE = (200,200)

N = 100 # number of creatures
D = 15 # number of cells infected at start time
R = 0.1 # percentage of creatures that move faster
REGULAR_MOVEMENT = 1 # the regular movement
FASTER_MOVEMENT = 10 # the faster movement
X = 10 # number of generations until recovery
P_1 = 0.01 # probability of infection during low infections
P_2 = 0.005 # probability of infection during high infections
T = 0.6 # threshold value for the change of P as a function of the disease state

