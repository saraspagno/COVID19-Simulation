import random
import numpy as np
from enum import Enum


class States(Enum):
    EMPTY = 0
    HEALTHY = 1
    SICK = 2
    RECOVERED = 3


SIZE = (200, 200)
N = 100
D = 15
R = 0.1
X = 10
P_1 = 0.01
P_2 = 0.005
T = 0.6
FASTER = 10


class Cell(object):
    """
    """

    def __init__(self, table, **kwargs):
        self.set_defaults(table, **kwargs)
        self.print_new_cell()

    def set_defaults(self, table, state=0, range=1):
        self.update = False
        self.range = range
        self.place_x = 0
        self.place_y = 0
        self.check_location(table)
        self.state = state

    def save(self):
        raise NotImplementedError

    def find_new_place(self, size=SIZE):
        x_range = (-min(size[0], self.place_x), min(SIZE[0] - self.place_x, size[0] - 1))
        y_range = (-min(self.place_y, size[1]), min(SIZE[1] - self.place_y, size[1] - 1))
        return [random.randint(x_range[0], x_range[1]), random.randint(y_range[0], y_range[1])]

    def check_location(self, table, size=SIZE):
        new_place = self.find_new_place()
        while table[new_place[0]][new_place[1]] != None:
            self.find_new_place(size)
        self.place_x, self.place_y = new_place

    def set_state(self, state):
        self.state = state

    def get_location(self):
        return (self.place_x, self.place_y)

    def load(self):
        raise NotImplementedError

    def update(self, N):
        current_place = (self.place_x, self.place_y)
        self.place_x = random.randint(-self.range, self.range)
        self.place_y = random.randint(-self.range, self.range)
        if self.update:
            self.N += 1
        if self.N == N:
            self.N = 0

    def print_new_cell(self):
        print("new ", self.state, " at ", self.place_x, self.place_y, "with movement capabil;ities of ", self.range)


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

    def __init__(self, **kwargs):
        self.set_defaults()
        self.__dict__.update(kwargs)
        self.initiate_board()

    def set_defaults(self):
        self.creatures = []
        # self.board = plt.table()
        self.board = np.array([[States.EMPTY for i in range(SIZE[0])] for j in range(SIZE[1])])

    def save(self):
        raise NotImplementedError

    def load(self):
        raise NotImplementedError

    def initiate_board(self):
        states = random.choices(["HEALTHY", "SICK"], weights=[1 - R, R], k=N)
        # np.array([None for i in range(N)]) #a list of N creatures # pd.DataFrame(columns=["place", "range", "state"]) #
        for state in states[0:N * D]:
            # place= self.check_location()
            cell = Cell(self.board, state=state, range=FASTER)
            # cell=pd.DataFrame({"place": [place], "range":[FASTER], "state": [state]})

            self.board[cell.place_x, cell.place_y] = cell.state
            self.creatures.append(cell)
        for state in states[N * D:]:
            cell = Cell(self.board, state=state)
            self.board[cell.place_x, cell.place_y] = cell.state
            self.creatures.append(cell)

    #
    def print_board(self):
        for j in range(SIZE[0]):
            for i in range(SIZE[1]):
                if self.board[i, j] != None:
                    print(self.board[i, j].state, end="|")
                else:
                    print("None", end="|")
            print("\n")

    def find_new_place(self, place, size=SIZE):
        x_range = (-min(size[0], place[0]), min(SIZE[0] - place[0], size[0] - 1))
        y_range = (-min(place[1], size[1]), min(SIZE[1] - place[1], size[1] - 1))
        return [random.randint(x_range[0], x_range[1]), random.randint(y_range[0], y_range[1])]

    def check_location(self, place=(0, 0), size=SIZE):
        new_place = self.find_new_place(place)
        while self.board[new_place[0]][new_place[1]] != None:
            self.find_new_place(place, size)
        return new_place


if __name__ == '__main__':
    print("hello world")
    # board = Board()
    # map(board)
    # board.creatures.
