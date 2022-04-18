import constant
import random

SIZE = constant.SIZE
States = constant.States
class Cell(object):
    """
    """

    def __init__(self, table, **kwargs):
        self.set_defaults(table,**kwargs)
        self.print_new_cell()

    def set_defaults(self, table, state, range ):
        self.update = False
        self.range = range
        self.place_x=0
        self.place_y=0
        self.check_location(table, move=(0, SIZE[0]))
        self.state = state
        if state == States.SICK:
            self.generation_num = 1
        else:
            self.generation_num = 0

        # self.neighbors

    def find_new_place(self, move):
        self.place_x = (self.place_x + random.randint(move[0], move[1])) % SIZE[1]
        self.place_y = (self.place_y + random.randint(move[0], move[1])) % SIZE[0]
        return [self.place_x, self.place_y]


    # def find_new_place(self, size=SIZE):
    #     x_range = (-min(size[0], self.place_x), min(SIZE[0] - self.place_x, size[0] -1))
    #     y_range = (-min(self.place_y, size[1]), min(SIZE[1] - self.place_y, size[1] -1))
    #     return [random.randint(x_range[0], x_range[1]), random.randint(y_range[0], y_range[1])]

    def check_location(self, table, move):
        new_place = self.find_new_place(move)
        while table[new_place] != States.EMPTY:
            self.find_new_place(move)
        self.set_location(new_place)

    def neighbors_states(self, table):
        if self.state == States.SICK:
            if self.generation_num == constant.X:
                self.state = States.RECOVERED
            else:
                self.generation_num += 1
        elif self.state == States.HEALTHY:
            neighbors = [-1, 0, 1]
            neighbors_sick = 0
            for i in neighbors:
                for j in neighbors:
                    place_x = self.place_x + i
                    place_y = self.place_y + j
                    if table[place_x, place_y] == States.SICK:
                        neighbors_sick += 1
            if neighbors_sick*constant


    def set_state(self, state):
        self.state = state

    def get_state(self):
        return self.state

    def set_location(self, new_place):
        self.place_x, self.place_y = new_place

    def get_location(self):
        return (self.place_x, self.place_y)

    def print_new_cell(self):
        print("new ", self.state, " at ", self.place_x, self.place_y, "with movement capabilities of ", self.range)
