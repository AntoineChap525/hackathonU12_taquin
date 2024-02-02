#Opérations sur les listes qu'on utilise par la suite pour le jeu de Taquin

#une fonction qui concatène les éléments d'une liste de taille 3*3 et les transforme en string,
#et renvoie aussi le couple qui donne les coordonnées du 0

# def concatene(liste):
#     res = ""
#     for i in range(3):
#         for j in range(3):
#             if liste[i][j] == 0:
#                 couple = (i , j)
#                 res += str(liste[i][j])
#             else:
#                 res += str(liste[i][j])
#     return res, couple

# print(concatene([[1, 2, 3], [4, 0, 5], [6, 7, 8]]))



def concatene(liste):
    chaine = ""
    for i in range(len(liste)):
        chaine += str(liste[i])
    return chaine, (liste.index(0)//3, liste.index(0)%3)

#print(concatene([1, 2, 3, 0, 4, 5, 6, 8, 7]))


#une fonction qui prend en argument deux chaines de caractères (0, 1 à 8) 
#et renvoie le caractère qui a pris la place du '0' dans la première chaîne, 
#sa position initiale et la position initiale du 0

def swap(chaine1, chaine2):
    for i in range(9):
        if chaine1[i] != chaine2[i] and chaine2[i] != "0" :
            return chaine2[i], i, chaine1.index(chaine2[i])

#print(swap("123450786", "123456780"))

def recherche(liste,element):
    for i in range(len(liste)):
        if liste[i]== element:
            return i
    return ("Erreur")

#fonction qui prend en argument une liste de taille 9 et la renvoie sous forme de liste de listes de taille 3*3

def from_list_to_tab(liste):
    tab = []
    for i in range(0, 9, 3):
        tab.append(liste[i:i+3])
    return tab

