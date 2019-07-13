import random
import pygame

WORKER_ANT = 0
WARRIOR_ANT = 1
MAGE_ANT = 2


class Ant:
    def __init__(self, world, pos, ant_type):
        self.world = world
        self.pos = pos
        self.type = ant_type

        self.image = self.get_img()

        self.counters = [int(world.population / 3), int(world.population / 3), int(world.population / 3)]
        self.counters[ant_type] += 1

        self.changed = False

    def get_img(self):
        if self.type == WORKER_ANT:
            return pygame.image.load("img/totally_free_worker_ant.png")
        if self.type == WARRIOR_ANT:
            return pygame.image.load("img/totally_free_warrior_ant.png")
        if self.type == MAGE_ANT:
            return pygame.image.load("img/totally_free_mage_ant.png")

    def balance_type(self):
        if min(self.counters) < 0.5 * max(self.counters):
            self.type = self.counters.index(min(self.counters))
            self.image = self.get_img()

    def check_surrounding(self):
        for y in (-1, 0, 1):
            for x in (-1, 0, 1):
                if (0 <= self.pos[0] + x < self.world.world_size
                        and 0 <= self.pos[1] + y < self.world.world_size
                        and self.world.map[self.pos[1] + y][self.pos[0] + x] is not None
                        and not (x == 0 and y == 0)):
                    self.counters[self.world.map[self.pos[1] + y][self.pos[0] + x].type] += 1

        self.balance_type()

    def get_valid_moves(self):
        possible_moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        moves = [(0, 0)]

        for move in possible_moves:
            x_move, y_move = move
            if (0 <= self.pos[0] + x_move < self.world.world_size and 0 <= self.pos[1] + y_move < self.world.world_size
                    and self.world.map[self.pos[1] + y_move][self.pos[0] + x_move] is None):
                moves.append(move)

        return moves

    def move(self):
        if self.changed:
            self.changed = False
            return

        x_move, y_move = random.choice(self.get_valid_moves())

        # Erases reference on current position and moves to right place
        self.world.map[self.pos[1]][self.pos[0]] = None
        self.pos = [self.pos[0] + x_move, self.pos[1] + y_move]
        self.world.map[self.pos[1]][self.pos[0]] = self

    def draw(self, tela):
        tela.blit(self.image, dest=(18 * self.pos[0], 18 * self.pos[1]))
