import flet as ft
import time
import os
import random
import solver2
import op_surlistes
import is_possible






#pos_list désigne la position dans la liste de l'élément à déplacer avec 0
#pos_list_0 désigne la position dans la liste de l'élément 0
#num désigne le numéro (1 à 8) de l'élément à déplacer
#lis_num est la liste des numéros des éléments
#list_container est la liste des containers






 

def main(page: ft.Page):
    
    def anim(list_num,list_container,num,pos_list,pos_list_0):
        x0,y0=int(pos_list_0%3),int(pos_list_0//3)
        x,y=int(pos_list%3),int(pos_list//3)
        n0=op_surlistes.recherche(list_num,0)
        n=op_surlistes.recherche(list_num,int(num))
        list_container[n0].left = 110*x
        list_container[n0].top = 110*y
        list_container[n].left = 110*x0
        list_container[n].top = 110*y0
        page.update()

    
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
    while (is_possible.is_possible(op_surlistes.from_list_to_tab(liste), (liste.index(0)//3, liste.index(0)%3))) == False:
        random.shuffle(liste)
        print("C'est impossible")



    r = []
    for i in range(0, 9):
        text_value = str(liste[i])
        text_height = 25
        if liste[i] == 0:
            c = ft.Container(ft.Text(str(liste[i]), text_align=ft.TextAlign.CENTER, size=70), width=100, height=100, bgcolor="red", top=lis[i][0], left=lis[i][1])
        else:
            c = ft.Container(ft.Text(str(liste[i]), text_align=ft.TextAlign.CENTER, size=70), width=100, height=100, bgcolor="blue", top=lis[i][0], left=lis[i][1])
        r.append(c)


    page.add(ft.Stack(r,height=330,width=330))
    page.add(ft.Row(controls=[ft.IconButton(ft.icons.NOT_STARTED_OUTLINED)]))
    page.update()
    print(r)



    
#on donne les positions initiales à la fonction solveur qui renvoie les positions successives 
    positions_successives = solver2.solve(op_surlistes.concatene(liste),solver2.solution) #liste des positions successives des cases



    for i in range(len(positions_successives)-1):
        print(positions_successives[i])
        num,pos_init,pos_fin=op_surlistes.swap(positions_successives[i],positions_successives[i+1])
        anim(liste,r,num,pos_init,pos_fin)
        time.sleep(1)
        page.update()




ft.app(target=main)




