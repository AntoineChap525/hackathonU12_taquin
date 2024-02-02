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
            c = ft.Container(ft.Text(liste[i], text_align=ft.TextAlign.CENTER), width=100, height=100, bgcolor="red", top=lis[i][0], left=lis[i][1])
        else:
            c = ft.Container(ft.Text(liste[i], text_align=ft.TextAlign.CENTER), width=100, height=100, bgcolor="blue", top=lis[i][0], left=lis[i][1])
        r.append(c)

    #print(r)
    page.update()
    page.add(ft.Stack(r,height=330,width=330))
    page.add(ft.Row(controls=[ft.IconButton(ft.icons.NOT_STARTED_OUTLINED)]))
    anim(liste,r,1,1,0)
    
    
    page.update()


def recherche(liste,element):
    for i in range(len(liste)):
        if liste[i]==element:
            return i
    return ("Erreur")

#pos_list désigne la position dans la liste de l'élément à déplacer avec 0
#pos_list_0 désigne la position dans la liste de l'élément 0
#num désigne le numéro (1 à 8) de l'élément à déplacer
#lis_num est la liste des numéros des éléments
#list_container est la liste des containers


def anim(lis_num,list_container,num,pos_list,pos_list_0):
    x0,y0=pos_list_0%3,pos_list_0//3
    x,y=pos_list%3,pos_list//3
    n0=recherche(list_num,0)
    n=recherche(list_num,num)
    list_container[n0]=ft.Container(ft.Text(0, text_align=ft.TextAlign.CENTER), width=100, height=100, bgcolor="red", top=x0*110, left=y0*110)
    list_container[n]=ft.Container(ft.Text(num, text_align=ft.TextAlign.CENTER), width=100, height=100, bgcolor="blue", top=x*110, left=y*110)
    page.add(ft.Stack(r,height=330,width=330))





ft.app(target=main)




