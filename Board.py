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
    """

    def __init__(self, R=constant.R, N=constant.N, D=constant.D, grid=None):
        """
        :param R: percentage of creatures with greater distance
        :param N: number of creatures
        :param D: percentage of starting infected
        :param grid: the starting grid
        """
        self.creatures = {}
        self.sick_creatures = int((D * N) / 100)
        self.recovered = 0
        if grid is None:
            self.grid = np.array([[int(States.EMPTY) for i in range(SIZE[0])] for j in range(SIZE[1])])
            self.initiate_board(R, N)
        else:
            self.grid = grid

    def initiate_board(self, R, N):
        """
        this method generates creatures such that R out of the N can move faster and a total of D are sick
            it saves the creatures in a dict and places all of the states on the board in the right place
        :param R: percentage of creatures that can move faster
        :param N: number of creatures
        :return:
        """
        # draw random ranges for N creatures according to R (percentage of creatures that can move faster)
        movements = random.choices([REGULAR_MOVEMENT, FASTER_MOVEMENT], weights=[1 - R/float(100), R/float(100)], k=N)

        # initiate board with the drawn ranges where sick_creatures are sick and the rest are healthy
        for movement in movements[0:self.sick_creatures]:
            cell = Cell.Cell(self.grid, state=int(States.SICK), movement=movement)
            self.grid[cell.place_x, cell.place_y] = cell.state
            self.creatures[(cell.place_x, cell.place_y)] = cell
        for movement in movements[self.sick_creatures:]:
            cell = Cell.Cell(self.grid, state=int(States.HEALTHY), movement=movement)
            self.grid[cell.place_x, cell.place_y] = cell.state
            self.creatures[(cell.place_x, cell.place_y)] = cell

    def create_copy(self, new_grid):
        """
        this method can be used to copy an existing board with same parameters, but providing a new grid
        :param new_grid: the grid to copy
        :return:
        """
        new_board = Board(grid=new_grid)
        new_board.sick_creatures = self.sick_creatures
        new_board.creatures = self.creatures
        new_board.recovered = self.recovered
        return new_board
