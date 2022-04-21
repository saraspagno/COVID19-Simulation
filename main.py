import numpy as np
import copy
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
    # First graph - animation
    grid = board.grid
    grid[0, 0] = 3

    fig1, ax1 = plt.subplots()
    ax1.axis('off')

    white_empty = Line2D([], [], marker="s", markersize=5, linewidth=0, color="w")
    green_healthy = Line2D([], [], marker="s", markersize=5, linewidth=0, color="g")
    red_infected = Line2D([], [], marker="s", markersize=5, linewidth=0, color="r")
    blue_recovered = Line2D([], [], marker="s", markersize=5, linewidth=0, color="b")
    ax1.legend((white_empty, green_healthy, red_infected, blue_recovered),
               ('Empty', 'Healthy', 'Infected', 'Recovered'),
               loc='upper left')

    cmap = ListedColormap(['w', 'g', 'r', 'b'])
    mat1 = ax1.matshow(grid, cmap=cmap)

    figManager = plt.get_current_fig_manager()
    figManager.window.showMaximized()

    # Second graph - infected

    global infected
    infected = [constant.D]
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(1, 1, 1)
    ax2.set_xlabel("Generations")
    ax2.set_ylabel("Infected")
    ax2.set_title("Number of Infected per Generation")
    ani2 = animation.FuncAnimation(fig2, generation, fargs=(mat1, ax2), frames=200, interval=40, save_count=50,
                                   repeat=False)
    ani = animation.FuncAnimation(fig1, generation, fargs=(mat1, ax2), frames=200, interval=40, save_count=50,
                                  repeat=False)

    plt.show()


def move(board):
    """
    this method moves all creatures on the board
    :param board: the board that contains the creatures and the board with the creatures's states
    :return: a new board with the new locations
    """
    new_grid = np.array([[States.EMPTY for i in range(SIZE[0])] for j in range(SIZE[1])])
    for creature in board.creatures.values():
        creature.check_location(new_grid, move=(-creature.range, creature.range))
        new_grid[creature.place_x, creature.place_y] = creature.state
    return new_grid


def generation(d, mat1, ax2):
    """
    this method represents a generation in the population's life
        in each generation the creatures move (according to their movement capabilities)
        and each creature's state can stay unchanged or be changed:
            from sick to recovered after 10 generations
            from healthy to sick according to it's neighbors
    :param d: standard for animation
    :return:
    """
    global board
    percentage = (board.sick_creatures / constant.N) * 100
    # example: if more than 10% infected, then P_2 (the lowest)
    if percentage > constant.T:
        print(f"HIGH PERCENTAGE: {percentage}, LOW PROBABILITY: {constant.P_2}")
        probability_of_infection = constant.P_2
    else:
        print(f"LOW PERCENTAGE: {percentage}, HIGH PROBABILITY: {constant.P_1}")
        probability_of_infection = constant.P_1
    new_grid = move(board)
    new_board = board.create_copy(new_grid)
    for creature in new_board.creatures.values():
        creature.infect_by_neighbors_states(board.grid, new_board, probability_of_infection)

    # adding to global for graph
    infected.append(new_board.sick_creatures)
    ax2.plot(infected, 'b')
    mat1.set_data(new_board.grid)
    board = new_board
    return mat1


if __name__ == '__main__':
    board = Board.Board(R=constant.R, N=constant.N, D=constant.D)
    print("After init!")
    show_board(board)
