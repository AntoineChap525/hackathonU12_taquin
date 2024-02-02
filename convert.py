from math import sqrt

def from_tab_to_str(tab):
    string = ""
    for elt in tab:
        for number in elt:
            string += str(number)
    return string

def from_str_to_tab(string):
    n = int(sqrt(len(string)))
    tab = [[None]*n]*n
    for i in range(n):
        for j in range(n):
            tab[i][j] = string[n*i+j]
    return tab