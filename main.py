import numpy as np
from matplotlib.colors import ListedColormap

import Board
import constant
import Console

import matplotlib
from matplotlib.lines import Line2D
import matplotlib.pyplot as plt
import matplotlib.animation as animation
matplotlib.use('qt5agg')

SIZE = constant.SIZE
States = constant.States
REGULAR_MOVEMENT = constant.REGULAR_MOVEMENT
FASTER_MOVEMENT = constant.FASTER_MOVEMENT


def show_board(grid):
    """
    this method show the animation and graphs of the simulation
    :param grid: the grid to show
    """
    # creating string with parameters to add to graphs
    parameters = f"N = {constant.N}\nD = {constant.D}\nR = {constant.R}\nX = {constant.X}\nP_1 = {constant.P_1}\nP_2 = {constant.P_2}\nT = {constant.T}\n "

    # First graph - animation
    grid[0, 0] = 3
    fig1, ax1 = plt.subplots()
    ax1.axis('off')
    # legend for first graph
    white_empty = Line2D([], [], marker="s", markersize=5, linewidth=0, color="w")
    green_healthy = Line2D([], [], marker="s", markersize=5, linewidth=0, color="g")
    red_infected = Line2D([], [], marker="s", markersize=5, linewidth=0, color="r")
    blue_recovered = Line2D([], [], marker="s", markersize=5, linewidth=0, color="b")
    ax1.legend((white_empty, green_healthy, red_infected, blue_recovered),
               ('Empty', 'Healthy', 'Infected', 'Recovered'),
               loc='upper left')

    cmap = ListedColormap(['w', 'g', 'r', 'b'])
    mat1 = ax1.matshow(grid, cmap=cmap)
    ax1.text(0.91, 0.5, parameters, fontsize=6, transform=plt.gcf().transFigure)
    ax1.set_title("COVID-19 Cellular Automata Simulation")

    mngr = plt.get_current_fig_manager()
    geom = mngr.window.geometry()
    x, y, dx, dy = geom.getRect()
    mngr.window.setGeometry(50, 100, dx, dy)

    # Second graph - infected
    global infected
    infected = [(constant.D / constant.N) * 100]
    fig2 = plt.figure()
    ax2 = fig2.add_subplot(1, 1, 1)
    ax2.set_xlabel("Generations")
    ax2.set_ylabel("Number of infected")
    ax2.set_title("Number of Infected per Generation")
    ax2.text(0.91, 0.5, parameters, fontsize=6, transform=plt.gcf().transFigure)

    # Third graph - infected percentage over available population
    global infected_per
    infected_per = [constant.D]
    fig3 = plt.figure()
    ax3 = fig3.add_subplot(1, 1, 1)
    ax3.set_xlabel("Generations")
    ax3.set_ylabel("Percentage of infected")
    ax3.set_title("Percentage of Infected per Generation")
    ax3.text(0.91, 0.5, parameters, fontsize=6, transform=plt.gcf().transFigure)
    mngr = plt.get_current_fig_manager()
    mngr.window.setGeometry(dx, 100, dx, dy)

    ani1 = animation.FuncAnimation(fig3, generation, fargs=(mat1, ax2, ax3), frames=150, interval=40, save_count=50,
                                   repeat=False)
    ani2 = animation.FuncAnimation(fig2, generation, fargs=(mat1, ax2, ax3), frames=150, interval=40, save_count=50,
                                   repeat=False)
    ani3 = animation.FuncAnimation(fig1, generation, fargs=(mat1, ax2, ax3), frames=150, interval=40, save_count=50,
                                   repeat=False)

    plt.show()


def move():
    """
    this method moves all creatures on the board
    :return: a new board with the new locations
    """
    new_grid = np.array([[States.EMPTY for i in range(SIZE[0])] for j in range(SIZE[1])])
    for creature in board.creatures.values():
        creature.check_location(new_grid, move=(-creature.range, creature.range))
        new_grid[creature.place_x, creature.place_y] = creature.state
    return new_grid


def generation(d, mat1, ax2, ax3):
    """
    this method represents a generation in the population's life
        in each generation the creatures move (according to their movement capabilities)
        and each creature's state can stay unchanged or be changed:
            from sick to recovered after 10 generations
            from healthy to sick according to it's neighbors
    :param d: standard for animation
    :param mat1: simulation for animation
    :param ax2: infected graph for animation
    :param ax3: percentage of infected graph for animation
    :return:
    """
    global board
    percentage = (board.sick_creatures / (constant.N - board.recovered)) * 100
    # example: if more than 10% infected, then P_2 (the lowest)
    if percentage > constant.T:
        if constant.P != constant.P_2:
            constant.P = constant.P_2
            constant.T = constant.T - constant.C
    else:
        if constant.P != constant.P_1:
            constant.P = constant.P_1
            constant.T = constant.T + constant.C
    new_grid = move()
    new_board = board.create_copy(new_grid)
    for creature in new_board.creatures.values():
        creature.infect_by_neighbors_states(board.grid, new_board, constant.P)

    # adding to global for graph
    if new_board.sick_creatures != 0:
        infected.append(new_board.sick_creatures)
    ax2.plot(infected, color='#25666F')
    ax2.fill_between([i for i in range(len(infected))], infected, color='#25666F')
    percentage = (new_board.sick_creatures / (constant.N - new_board.recovered)) * 100
    if percentage != 0:
        infected_per.append((new_board.sick_creatures / (constant.N - new_board.recovered)) * 100)
    ax3.plot(infected_per, 'r')
    ax3.fill_between([i for i in range(len(infected_per))], infected_per, color='#FC494F')
    mat1.set_data(new_board.grid)
    board = new_board
    return mat1

if __name__ == '__main__':
    Console.start_console()
    print(constant.these_parameters)
    board = Board.Board(R=constant.R, N=constant.N, D=constant.D)
    show_board(board.grid)
