from math import sqrt

def from_tab_to_str(tab):
    string = ""
    for elt in tab:
        for number in elt:
            string += str(number)
    return string

def from_str_to_tab(string):
    n = int(sqrt(len(string)))
    tab = [[None]*n for _ in range(n)]
    for j in range(n):
        for i in range(n):
            tab[i][j] = string[n*i + j]
    return tab

def neighbours(taquin, coord):
    taquin = from_str_to_tab(taquin)
    n = len(taquin)
    i, j = coord
    neigh = []
    for s in [-1, 1]:
        taqu2 = [row[:] for row in taquin]
        if i+s >= 0 and i+s < n:
            taqu2[i + s][j], taqu2[i][j] = taqu2[i][j], taqu2[i + s][j]
            neigh.append(from_tab_to_str(taqu2))

    for s in [-1, 1]:
        taqu2 = [row[:] for row in taquin]
        if j+s >= 0 and j+s < n:
            taqu2[i][j + s], taqu2[i][j] = taqu2[i][j], taqu2[i][j + s]
            neigh.append(from_tab_to_str(taqu2))
    return neigh
