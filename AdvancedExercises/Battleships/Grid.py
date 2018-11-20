from abc import ABC

class Grid(ABC):
    def __init__(self, x, y):
        self.grid = [[0] * x] * y

    def prompt_front_x(self):

        condition = False

        while condition:

            front_x = input("Where would you like to position the front of the boat on the x_axis" \
                            + " (" + str("0 <= x <= ") + str(len(self.grid[0])) + ")")

            if 0 <= int(front_x) <= len(self.grid[0]):
                condition = True
            else:
                else:
                print("Please select a valid value for x. \n")

    def prompt_front_y(self):

        condition = False

        while condition:

            front_y = input("Where would you like to position the front of the boat on the y_axis" \
                            + " (" + str("0 <= y <= ") + str(len(self.grid)) + ")")

            if 0 <= int(front_y) <= len(self.grid):
                condition = True
            else:
                print("Please select a valid value for y. \n")







    def add_patrol_boat(self):
        pass

    def add_battleship(self):
        pass

    def add_submarine(self):
        pass

    def add_destroyer(self):
        pass

    def add_carrier(self):
        pass

a = Grid(5,7)
a.position()