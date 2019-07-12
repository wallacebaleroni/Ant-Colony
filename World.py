import random

# Constraints
EMPTY_SPACE = 0
ANT = 1


class World:
    def __init__(self, world_size, population):
        self.world_size = world_size
        self.population = population

        self.world = [[0 for y in range(world_size)] for x in range(world_size)]

        self.populate()

    def show(self):
        for line in self.world:
            for cell in line:
                print("%d " % cell, end="")
            print()
        print()

    def populate(self):
        for i in range(self.population):
            unused_cell = False
            while not unused_cell:
                x, y = random.randint(0, 9), random.randint(0, 9)
                if self.world[y][x] == EMPTY_SPACE:
                    unused_cell = True
                    self.world[y][x] = ANT

    def get_valid_moves(self, x, y):
        moves = [(0, 0)]

        for y_move in (-1, 0, 1):
            for x_move in (-1, 0, 1):
                if (0 <= x + x_move < self.world_size
                        and 0 <= y + y_move < self.world_size
                        and self.world[y + y_move][x + x_move] == EMPTY_SPACE):
                    moves.append((x_move, y_move))

        return moves

    def move_ants(self):
        for y in range(self.world_size):
            for x in range(self.world_size):
                if self.world[y][x] == ANT:
                    moves = self.get_valid_moves(x, y)

                    x_move, y_move = random.choice(moves)

                    self.world[y][x] = EMPTY_SPACE
                    self.world[y + y_move][x + x_move] = ANT
