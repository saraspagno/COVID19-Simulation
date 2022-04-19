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

    def __init__(self, sick_creatures=constant.D, creatures= {}):
        """
        :param R: percentage of creatures that can move faster
        :param N: number of creatures
        :param sick_creatures: number of cells infected at start time (represented as D in the constants)
        """
        self.creatures = creatures
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
        # draw random ranges for N creatures according to R (percentage of creatures that can move faster)
        movements = random.choices([REGULAR_MOVEMENT, FASTER_MOVEMENT], weights=[1 - R, R], k=N)

        # initiate board with the drawn ranges where D creatures are sick and the rest are healthy
        for movement in movements[0:self.sick_creatures - 1]:
            cell = Cell.Cell(self.board, state=States.SICK, movement=movement)
            self.change_state_in_cell([cell.place_x, cell.place_y], cell.state)
            self.set_creatures_list([cell.place_x, cell.place_y], cell)
            # self.board[cell.place_x, cell.place_y] = cell.state
            # self.creatures[(cell.place_x, cell.place_y)] = cell
        for movement in movements[self.sick_creatures:]:
            cell = Cell.Cell(self.board, state=States.HEALTHY, movement=movement)
            self.change_state_in_cell([cell.place_x, cell.place_y], cell.state)
            self.set_creatures_list([cell.place_x, cell.place_y], cell)
            # self.board[cell.place_x, cell.place_y] = cell.state
            # self.creatures[(cell.place_x, cell.place_y)] = cell

    def set_num_of_sick(self, new_num):
        self.sick_creatures = new_num

    def change_state_in_cell(self, place, new_state):
        self.board[place] = new_state

    def set_creatures_list(self, place, changed_creature):
        self.creatures[place] = changed_creature

    def print_board(self):
        """
            you need to make this work, this is not it!!
        :return:
        """
        for j in range(SIZE[0]):
            for i in range(SIZE[1]):
                if self.board[i, j] is not None:
                    print(self.board[i, j].state, end="|")
                else:
                    print("None", end="|")
            print("\n")
