import time

from World import *

# Parameters
WORLD_SIZE = 40
POPULATION = 100

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
    world = World(WORLD_SIZE, POPULATION)

    pygame.init()

    tela = pygame.display.set_mode([720, 720])

    world.show(tela)

    running = True
    while running:
        world.move_ants()
        world.check_classes()

        world.show(tela)

        running = handle_events(pygame.event.get())

        pygame.display.flip()

        time.sleep(0.05)


main()
