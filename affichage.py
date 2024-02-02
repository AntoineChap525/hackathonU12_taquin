import flet as ft
import time
import os
import random


 

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    t = ft.Text(value="Jeu de Taquin", color="red")
    lis=[]
    # on place les carrés tout les 60 pixels
    #on crée la liste des positions possibles
    for i in range(3):
        for j in range(3):
            lis.append([i*110,j*110])
    
    #on mélange la liste
    liste=[0,1,2,3,4,5,6,7,8]
    random.shuffle(liste)
    r = []
    for i in range(0,9):
        if liste[i]==0:
            c=ft.Container(ft.Text(liste[i]),width=100, height=100, bgcolor="red", top=lis[i][0], left=lis[i][1])
        else :
            c=ft.Container(ft.Text(liste[i]),width=100, height=100, bgcolor="blue", top=lis[i][0], left=lis[i][1])
        r.append(c)

    print(liste)
    page.update()
    page.add(ft.Stack(r,height=330,width=330))
    page.add(ft.Row(controls=[ft.IconButton(ft.icons.NOT_STARTED_OUTLINED)]))


#on donne les positions initiales à la fonction solveur qui renvoie les positions successives 
    positions_successives = [] #liste des positions successives des cases

#on affiche chacune des positions successives des cases via flet
    for i in range(len(positions_successives)):
        r = []
        for j in range(9):
            if positions_successives[i][j]==0:
                c=ft.Container(ft.Text(positions_successives[i][j]),width=100, height=100, bgcolor="red", top=lis[j][0], left=lis[j][1])
            else :
                c=ft.Container(ft.Text(positions_successives[i][j]),width=100, height=100, bgcolor="blue", top=lis[j][0], left=lis[j][1])
            r.append(c) 
    


    page.update()

ft.app(target=main)




