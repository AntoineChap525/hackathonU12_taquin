import flet as ft
import time
import solver2
import op_surlistes
import random

def get_empty_position(taquin):
    for i, row in enumerate(taquin):
        for j, value in enumerate(row):
            if value == 0:
                return i, j

def anim(liste, list_container, num, pos_init, pos_fin):
    x0, y0 = pos_init % 3, pos_init // 3
    x, y = pos_fin % 3, pos_fin // 3
    n0 = op_surlistes.recherche(liste, 0)
    n = op_surlistes.recherche(liste, num)
    list_container[n0] = ft.Container(ft.Text(0, text_align=ft.TextAlign.CENTER), width=100, height=100, bgcolor="red", top=x * 110, left=y * 110)
    list_container[n] = ft.Container(ft.Text(num, text_align=ft.TextAlign.CENTER, size=70), width=100, height=100, bgcolor="blue", top=x0 * 110, left=y0 * 110)

def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    t = ft.Text(value="Jeu de Taquin", color="red")
    lis = []

    for i in range(3):
        for j in range(3):
            lis.append([i * 110, j * 110])

    liste = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    random.shuffle(liste)
    r = []

    for i in range(0, 9):
        text_value = str(liste[i])
        text_height = 25
        if liste[i] == 0:
            c = ft.Container(ft.Text(str(liste[i]), text_align=ft.TextAlign.CENTER, size=70), width=100, height=100,
                             bgcolor="red", top=lis[i][0], left=lis[i][1])
        else:
            c = ft.Container(ft.Text(str(liste[i]), text_align=ft.TextAlign.CENTER, size=70), width=100, height=100,
                             bgcolor="blue", top=lis[i][0], left=lis[i][1])
        r.append(c)

    page.update()
    stack = ft.Stack(r, height=330, width=330)
    page.add(stack)
    page.add(ft.Row(controls=[ft.IconButton(ft.icons.NOT_STARTED_OUTLINED)]))
    page.update()

    while True:
        event = page.wait_for_event()
        if event['type'] == 'key_down':
            direction = event['key'].upper()
            if direction == 'X':
                break
            elif direction in ["Z", "Q", "S", "D"]:
                i, j = get_empty_position(liste)
                if direction == "Z" and i > 0:
                    liste[i][j], liste[i - 1][j] = liste[i - 1][j], liste[i][j]
                elif direction == "S" and i < len(liste) - 1:
                    liste[i][j], liste[i + 1][j] = liste[i + 1][j], liste[i][j]
                elif direction == "Q" and j > 0:
                    liste[i][j], liste[i][j - 1] = liste[i][j - 1], liste[i][j]
                elif direction == "D" and j < len(liste[0]) - 1:
                    liste[i][j], liste[i][j + 1] = liste[i][j + 1], liste[i][j]
                anim(liste, r, 0, (i + 1) * 3 + j, i * 3 + j)
                page.update()

ft.app(target=main)
