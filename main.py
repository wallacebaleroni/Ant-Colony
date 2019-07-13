import time

from World import *

# Parameters
WORLD_SIZE = 40
POPULATION = 100
CHANGE_FACTOR = 0.5

WORKER_ANT = 0


def handle_events(events):
    for event in events:
        if event.type == pygame.QUIT:
            return False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                return False
    return True


def main():
    world = World(WORLD_SIZE, POPULATION, CHANGE_FACTOR)

    pygame.init()

    tela = pygame.display.set_mode([720, 720])

    world.show(tela)

    print("World size: %d" % WORLD_SIZE ** 2)
    print("Ants number: %d" % POPULATION)
    print("Change factor: %d%%" % (CHANGE_FACTOR * 100))
    print()

    running = True
    while running:
        world.move_ants()
        world.check_classes()

        world.show(tela)
        counter = world.get_count()
        print("WO: %d, WA: %d, MA: %d " % (counter[0], counter[1], counter[2]), end="\r")

        running = handle_events(pygame.event.get())

        pygame.display.flip()

        time.sleep(0.05)


main()
