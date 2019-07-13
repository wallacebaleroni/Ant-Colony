from Ant import *

# Constraints
EMPTY_SPACE = None


class World:
    def __init__(self, world_size, population):
        self.world_size = world_size
        self.population = population

        self.map = [[None for y in range(world_size)] for x in range(world_size)]

        self.populate()

    def check_classes(self):
        for y in range(self.world_size):
            for x in range(self.world_size):
                if self.map[y][x] is not None:
                    self.map[y][x].check_surrounding()

    def show(self, tela):
        tela.fill((0, 0, 0))

        for i in range(self.world_size):
            for j in range(self.world_size):
                if self.map[i][j] is not None:
                    self.map[i][j].draw(tela)

    def populate(self):
        for i in range(self.population):
            found_unused_cell = False
            while not found_unused_cell:
                x, y = random.randint(0, self.world_size - 1), random.randint(0, self.world_size - 1)
                if self.map[y][x] is None:
                    found_unused_cell = True
                    self.map[y][x] = Ant(pos=(x, y), world=self, ant_type=WORKER_ANT)

    def move_ants(self):
        for y in range(self.world_size):
            for x in range(self.world_size):
                if self.map[y][x] is not None:
                    self.map[y][x].move()
