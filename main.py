import numpy as np
from matplotlib.colors import ListedColormap

import Board
import constant

import matplotlib.cm as cm
import matplotlib
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
matplotlib.use('Qt5Agg')

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


def generation(d):
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
    board.board = move(board)
    for creature in board.creatures.values():
        creature.infect_by_neighbors_states(board.board, probability_of_infection)

    # show_board(board)

    global grid
    grid = board.board
    mat.set_data(grid)
    return mat





if __name__ == '__main__':
    board = Board.Board(R=constant.R, N=constant.N, sick_creatures=constant.D)
    gen = 0
    print("After init!")
    # while True:
    #     print("Generation: ", gen)
    #     gen += 1
    #     generation()

    grid = board.board
    grid[0, 0] = 3

    fig, ax = plt.subplots()
    ax.axis('off')
    row = 0

    white_empty = Line2D([], [], marker="s", markersize=5, linewidth=0, color="w")
    green_healthy = Line2D([], [], marker="s", markersize=5, linewidth=0, color="g")
    red_infected = Line2D([], [], marker="s", markersize=5, linewidth=0, color="r")
    blue_recovered = Line2D([], [], marker="s", markersize=5, linewidth=0, color="b")
    ax.legend((white_empty, green_healthy, red_infected, blue_recovered), ('Empty', 'Healthy', 'Infected', 'Recovered'), loc='upper left')

    cmap = ListedColormap(['w', 'g', 'r', 'b'])
    mat = ax.matshow(grid, cmap=cmap)
    ani = animation.FuncAnimation(fig, generation, interval=80, save_count=50, repeat=False)

    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()
    plt.show()
