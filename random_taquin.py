import random
from is_possible import is_possible


def find_zero(board: list):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                couple = (i, j)
    return couple


def create_random_grid():
    chiffres = list(range(0, 9))
    random.shuffle(chiffres)
    grille_aleatoire = [chiffres[i : i + 3] for i in range(0, 9, 3)]

    return grille_aleatoire


def pick_random_taquin():
    a = False
    while not a:
        random_grid = create_random_grid()
        zero = find_zero(random_grid)
        a = is_possible(random_grid, zero)
    grid = ""
    for line in random_grid:
        for j in line:
            grid += str(j)
    return grid, zero
