import constant
import random

SIZE = constant.SIZE
States = constant.States


class Cell(object):
    """
    this class represents a creature
    the fields it has are:
        range: the range of movement, either regular=1, or fast (R creturs)=10
        place_x: the creature's x location on the board
        place_y: the creature's y location on the board
        state: whether it is healthy, sick or recovered
        generation_num: the numbers of generations a creature has been sick (after 10 generations it is recovered)
    """

    def __init__(self, table, state, movement):
        self.range = movement
        self.place_x = 0
        self.place_y = 0
        self.check_location(table, move=(0, SIZE[0]))
        self.state = state
        if state == int(States.SICK):
            self.generation_num = 1
        else:
            self.generation_num = 0
        self.print_new_cell()

    def find_new_place(self, move):
        """
        this function finds a new random location within a certain range
            for initiation in is used with initial location of (0,0) and moving options of (0,200)
            for movement during the game it can move either 1 or 10 places from it's current location
        :param move: the range of movement, either regular=1, or fast (R creturs)=10, or 200 for the initiation
        :return: the new location
        """
        self.place_x = (self.place_x + random.randint(move[0], move[1])) % SIZE[1]
        self.place_y = (self.place_y + random.randint(move[0], move[1])) % SIZE[0]
        return self.place_x, self.place_y

    # def find_new_place(self, size=SIZE):
    #     x_range = (-min(size[0], self.place_x), min(SIZE[0] - self.place_x, size[0] -1))
    #     y_range = (-min(self.place_y, size[1]), min(SIZE[1] - self.place_y, size[1] -1))
    #     return [random.randint(x_range[0], x_range[1]), random.randint(y_range[0], y_range[1])]

    def check_location(self, board, move):
        """
        this function makes sure a location is not already occupied
            it draws a random location
            and as long as the location is occupied it draws a new location
        :param board: the board where the creature is located
        :param move: the range of movement, either regular=1, or fast (R creturs)=10
        :return:
        """
        new_x, new_y = self.find_new_place(move)
        while board[new_x][new_y] != int(States.EMPTY):
            new_x, new_y = self.find_new_place(move)
        self.set_location(new_x, new_y)

    def infect_by_neighbors_states(self, board, probability_of_infection):
        """
        a function that decides whether a cell is infected according to a it's neighbors and a probability_of_infection
        :param board: the board, in order to find all it's neighbors
        :param probability_of_infection: either P_1 or P_2, depending on the percentage of sick
        :return:
        """
        if self.state == int(States.SICK):
            if self.generation_num == constant.X:
                self.state = int(States.RECOVERED)
                self.state = States.RECOVERED
                return -1
            else:
                self.generation_num += 1
        elif self.state == int(States.HEALTHY):
            neighbors = [-1, 0, 1]
            neighbors_sick = 0
            for i in neighbors:
                for j in neighbors:
                    place_x = (self.place_x + i) % SIZE[1]
                    place_y = (self.place_y + j) % SIZE[0]
                    if board[place_x, place_y] == int(States.SICK):
                        neighbors_sick += 1
            probability_of_infection = neighbors_sick * probability_of_infection
            weights = [1 - probability_of_infection, probability_of_infection]
            self.set_state(random.choices([int(States.HEALTHY), int(States.SICK)], weights=weights, k=1)[0])
            state = random.choices([States.HEALTHY, States.SICK], weights=weights, k=1)
            self.set_state(state)
            if state == States.SICK:
                return 1
        return 0

    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_location(self, place_x, place_y):
        self.place_x, self.place_y = place_x, place_y

    def get_location(self):
        return self.place_x, self.place_y

    def print_new_cell(self):
        print("new ", self.state, " at ", self.place_x, self.place_y, "with movement capabilities of ", self.range)
