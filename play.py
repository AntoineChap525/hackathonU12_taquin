import pygame
import sys
import random

# Initialisation de Pygame
pygame.init()

# Dimensions de la fenêtre
WIDTH, HEIGHT = 300, 300

# Couleurs
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Taille des cases
CELL_SIZE = WIDTH // 3

# Initialisation de la fenêtre
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Jeu du Taquin")


# Données
def creer_grille_aleatoire():
    chiffres = list(range(1, 9))
    random.shuffle(chiffres)
    chiffres += [0]
    grille_aleatoire = [chiffres[i : i + 3] for i in range(0, 9, 3)]
    return grille_aleatoire


grille_jeu = creer_grille_aleatoire()

# Position de la case vide
case_vide = (2, 2)


# Fonction pour afficher la grille
def afficher_grille():
    screen.fill(WHITE)
    font = pygame.font.Font(None, 36)

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(
                screen, BLACK, (j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE), 2
            )

            if grille_jeu[i][j] != 0:
                text = font.render(str(grille_jeu[i][j]), True, BLACK)
                text_rect = text.get_rect(
                    center=(
                        j * CELL_SIZE + CELL_SIZE // 2,
                        i * CELL_SIZE + CELL_SIZE // 2,
                    )
                )
                screen.blit(text, text_rect)


# Fonction pour déplacer la case vide
def deplacer_case_vide(direction):
    global case_vide

    i, j = case_vide
    if direction == "UP" and i > 0:
        grille_jeu[i][j], grille_jeu[i - 1][j] = grille_jeu[i - 1][j], grille_jeu[i][j]
        case_vide = (i - 1, j)
    elif direction == "DOWN" and i < 2:
        grille_jeu[i][j], grille_jeu[i + 1][j] = grille_jeu[i + 1][j], grille_jeu[i][j]
        case_vide = (i + 1, j)
    elif direction == "LEFT" and j > 0:
        grille_jeu[i][j], grille_jeu[i][j - 1] = grille_jeu[i][j - 1], grille_jeu[i][j]
        case_vide = (i, j - 1)
    elif direction == "RIGHT" and j < 2:
        grille_jeu[i][j], grille_jeu[i][j + 1] = grille_jeu[i][j + 1], grille_jeu[i][j]
        case_vide = (i, j + 1)


# Boucle principale
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                deplacer_case_vide("DOWN")
            elif event.key == pygame.K_DOWN:
                deplacer_case_vide("UP")
            elif event.key == pygame.K_LEFT:
                deplacer_case_vide("RIGHT")
            elif event.key == pygame.K_RIGHT:
                deplacer_case_vide("LEFT")

    afficher_grille()
    pygame.display.flip()
