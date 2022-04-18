import numpy as np
import Board
import constant

SIZE = constant.SIZE
States = constant.States
REGULAR_MOVEMENT = constant.REGULAR_MOVEMENT
FASTER_MOVEMENT = constant.FASTER_MOVEMENT


def show_board(board):
    """
    :param board:
    :return:
    """
    board.print_board()


def move(board):
    """
    this method moves all creatures on the board
    :param board: the board that contains the creatures and the board with the creatures's states
    :return: a new board with the new locations
    """
    new_board = np.array([[States.EMPTY for i in range(SIZE[0])] for j in range(SIZE[1])])
    for creature in board.creatures.values():
        creature.check_location(new_board, move=(-creature.range, creature.range))
        new_board[creature.place_x, creature.place_y] = creature.state
    return new_board


def generation(board):
    """
    this method represents a generation in the population's life
        in each generation the creatures move (according to their movement capabilities)
        and each creature's state can stay unchanged or be changed:
            from sick to recovered after 10 generations
            from healthy to sick according to it's neighbors
    :param board: the board that contains the creatures and the board with the creature's states
    :return:
    """
    percentage = board.sick_creatures / constant.N
    if percentage > constant.T:
        probability_of_infection = constant.P_2
    else:
        probability_of_infection = constant.P_1
    move(board)
    for creature in board.creatures.values():
        creature.infect_by_neighbors_states(board, probability_of_infection)
    show_board(board)


if __name__ == '__main__':
    board = Board.Board(R=constant.R, N=constant.N, sick_creatures=constant.D)
    generation(board)
