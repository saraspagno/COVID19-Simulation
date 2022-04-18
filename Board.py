import constant
import random
import numpy as np
import Cell

SIZE = constant.SIZE
States = constant.States
REGULAR_MOVEMENT = constant.REGULAR_MOVEMENT
FASTER_MOVEMENT = constant.FASTER_MOVEMENT



class Board(object):
    """
    this class represents a board of 200X200 that contains creatures
    the fields it has are:
        board: the board that contains the states of the creatures
        creatures: a dict of creatures where
            the keys are the creature's locations
            the values are the creatures themselves
        sick_creatures: the number of sick creatures (the initial number is defined by D)
    """

    def __init__(self, R=constant.R, N = constant.N, sick_creatures = constant.D, **kwargs):
        """

        :param R: percentage of creatures that can move faster
        :param N: number of creatures
        :param sick_creatures: number of cells infected at start time (represented as D in the constants)
        :param kwargs:
        """
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
        """
        this method generates creatures such that R out of the N can move faster and a total of D are sick
            it saves the creatures in a dict and places all of the states on the board in the right place
        :param R: percentage of creatures that can move faster
        :param N: number of creatures
        :return:
        """
        ## draw random ranges for N creatures according to R (percentage of creatures that can move faster)
        movements = random.choices([REGULAR_MOVEMENT, FASTER_MOVEMENT], weights=[1 - R, R], k=N)

        ### initiate board with the drawn ranges where D creatures are sick and the rest are healthy
        for movement in movements[0:self.sick_creatures - 1]:
            cell = Cell.Cell(self.board, state=States.SICK, range=movement)
            self.board[cell.place_x, cell.place_y] = cell.state
            self.creatures[(cell.place_x, cell.place_y)] = cell
        for movement in movements[self.sick_creatures:]:
            cell = Cell.Cell(self.board, state=States.HEALTHY, range=movement)
            self.board[cell.place_x, cell.place_y] = cell.state
            self.creatures[(cell.place_x, cell.place_y)] = cell


    def print_board(self):
        for j in range(SIZE[0]):
            for i in range(SIZE[1]):
                if self.board[i, j] != None:
                    print(self.board[i, j].state, end="|")
                else:
                    print("None", end="|")
            print("\n")