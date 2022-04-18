import constant
import random
import numpy as np
import Cell

SIZE = constant.SIZE
States = constant.States
REGULAR_MOVEMENT = constant.REGULAR_MOVEMENT
FASTER_MOVEMENT = constant.FASTER_MOVEMENT



class Board(object):
    '''
    Implement the system and look for a combination of the parameters described above that will result in the behavior of waves (an increase and decrease in the number of patients), at least 3 times during the life of the simulation.
    The parameters are:
    N - number of creatures
    D - number of cells infected at start time
    R - percentage of creatures that can move faster
    X - number of generations until recovery
    P_1, P_2 - probability of infection during high and low infections
    T - threshold value for the change of P as a function of the disease state
    '''

    def __init__(self, R=constant.R, N = constant.N, sick_creatures = constant.D, **kwargs):
        self.set_defaults(sick_creatures)
        self.__dict__.update(kwargs)
        self.initiate_board(R, N)

    def set_defaults(self, sick_creatures):
        self.creatures = {}
        self.board = np.array([[States.EMPTY for i in range(SIZE[0])] for j in range(SIZE[1])])
        self.sick_creatures = sick_creatures

    def save(self):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError

    def initiate_board(self, R, N):
        ## draw random ranges for N creatures according to R (percentage of creatures that can move faster)
        movements = random.choices([REGULAR_MOVEMENT, FASTER_MOVEMENT], weights=[1 - R, R], k=N)

        ### initiate board with the drawn ranges where D creatures are sick and the rest are healthy
        for movement in movements[0:self.sick_creatures - 1]:
            cell = Cell(self.board, state=States.SICK, range=movement)
            self.board[cell.place_x, cell.place_y] = cell.state
            self.creatures[(cell.place_x, cell.place_y)] = cell
        for movement in movements[self.sick_creatures:]:
            cell = Cell(self.board, state=States.HEALTHY, range=movement)
            self.board[cell.place_x, cell.place_y] = cell.state
            self.creatures[(cell.place_x, cell.place_y)] = cell

    #
    def print_board(self):
        for j in range(SIZE[0]):
            for i in range(SIZE[1]):
                if self.board[i, j] != None:
                    print(self.board[i, j].state, end="|")
                else:
                    print("None", end="|")
            print("\n")
