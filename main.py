from World import *

# Parameters
WORLD_SIZE = 10
POPULATION = 10


def main():
    world = World(WORLD_SIZE, POPULATION)

    world.show()

    while True:
        world.move_ants()
        world.show()


main()
