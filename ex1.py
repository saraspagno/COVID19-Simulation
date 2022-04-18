import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import Board
import constant
import numpy as np
import Cell

SIZE = constant.SIZE
States = constant.States
REGULAR_MOVEMENT = constant.REGULAR_MOVEMENT
FASTER_MOVEMENT = constant.FASTER_MOVEMENT



def initiate_game():
    board = Board.Board(R=constant.R, N = constant.N, sick_creatures = constant.D)


def move(self):
    new_board = np.array([[States.EMPTY for i in range(SIZE[0])] for j in range(SIZE[1])])
    for creature in self.creatures.values():
        creature.check_location(new_board, move=(-creature.range,creature.range))
        new_board[creature.place_x, creature.place_y]=creature.state
    return new_board


if __name__ == '__main__':
    # board.creatures.
#
ֿ
