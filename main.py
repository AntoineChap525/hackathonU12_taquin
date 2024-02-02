import solver2

import pygame
import sys
import random_taquin
import convert
import find_neighbours
from is_possible import is_possible

# Initialisation of Pygame
pygame.init()

# Dimensions
WIDTH, HEIGHT = 300, 330

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Taquin
if len(sys.argv) > 1:
    non_valid = True
    taquin = sys.argv[1]
    while non_valid:
        tab = convert.from_str_to_tab(taquin)
        zero = find_neighbours.find_zero(tab)
        start = taquin, zero
        non_valid = not is_possible(taquin, zero)
        if non_valid:
            print("Taquin impossible !")
            taquin = input("Nouveau taquin:")

else:  # random taquin
    start = random_taquin.pick_random_taquin()
path = solver2.solve(start, solver2.solution)

# Screen initialisation
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Taquin Solver")


def display(path, n):
    screen.fill(WHITE)
    font = pygame.font.Font(None, 36)

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(screen, BLACK, (j * 100, i * 100, 100, 100), 2)
            number = path[n][3 * j + i]
            if number != "0":
                text = font.render(str(path[n][3 * j + i]), True, BLACK)
                text_rect = text.get_rect(center=(i * 100 + 50, j * 100 + 50))
                screen.blit(text, text_rect)
    text = font.render(str(n + 1) + "/" + str(len(path)), True, BLACK)
    text_rect = text.get_rect(center=(150, 315))
    screen.blit(text, text_rect)


n = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                # Passer à l'étape suivante
                if n < len(path) - 1:
                    n += 1
            if event.key == pygame.K_LEFT:
                # Passer à l'étape suivante
                if n > 0:
                    n -= 1

    display(path, n)
    pygame.display.flip()
