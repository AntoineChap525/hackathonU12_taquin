from math import sqrt


def from_tab_to_str(tab):
    string = ""
    for elt in tab:
        for number in elt:
            string += str(number)
    return string


def from_str_to_tab(string):
    n = int(sqrt(len(string)))
    tab = [[None] * n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            tab[i][j] = string[n * i + j]
    return tab


def find_zero(board: list):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == "0":
                couple = (i, j)
    return couple


def neighbours(taquin, coord):
    taquin = from_str_to_tab(taquin)
    n = len(taquin)
    i, j = coord
    neigh = []
    for s in [-1, 1]:
        taqu2 = [row[:] for row in taquin]
        if i + s >= 0 and i + s < n:
            taqu2[i + s][j], taqu2[i][j] = taqu2[i][j], taqu2[i + s][j]
<<<<<<< HEAD
            neigh.append([from_tab_to_str(taqu2),(i+s,j)])
=======
            zero = find_zero(taqu2)
            neigh.append((from_tab_to_str(taqu2), zero))
>>>>>>> 5bbe861ec7d36aaa914fe4d42f5bb270389af787

    for s in [-1, 1]:
        taqu2 = [row[:] for row in taquin]
        if j + s >= 0 and j + s < n:
            taqu2[i][j + s], taqu2[i][j] = taqu2[i][j], taqu2[i][j + s]
<<<<<<< HEAD
            neigh.append([from_tab_to_str(taqu2),(i,j+s)])
=======
            zero = find_zero(taqu2)
            neigh.append((from_tab_to_str(taqu2), zero))
>>>>>>> 5bbe861ec7d36aaa914fe4d42f5bb270389af787
    return neigh
