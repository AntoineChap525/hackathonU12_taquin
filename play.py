import pygame
import flet as ft
from pygame.locals import QUIT, KEYDOWN, K_z, K_q, K_s, K_d
import random

def draw_taquin(page: ft.Page, taquin):
    page.clear()
    
    lis = [[i * 110, j * 110] for i in range(3) for j in range(3)]

    for i in range(9):
        text_value = str(taquin[i])
        text_height = 25
        if taquin[i] != 0:
            c = ft.Container(
                ft.Text(str(taquin[i]), text_align=ft.TextAlign.CENTER, size=70),
                width=100, height=100, bgcolor="blue", top=lis[i][0], left=lis[i][1]
            )
            page.add(c)

    page.update()

def move_taquin(taquin, direction):
    empty_position = taquin.index(0)
    if direction == K_z and empty_position > 2:
        taquin[empty_position], taquin[empty_position - 3] = taquin[empty_position - 3], taquin[empty_position]
    elif direction == K_s and empty_position < 6:
        taquin[empty_position], taquin[empty_position + 3] = taquin[empty_position + 3], taquin[empty_position]
    elif direction == K_q and empty_position % 3 > 0:
        taquin[empty_position], taquin[empty_position - 1] = taquin[empty_position - 1], taquin[empty_position]
    elif direction == K_d and empty_position % 3 < 2:
        taquin[empty_position], taquin[empty_position + 1] = taquin[empty_position + 1], taquin[empty_position]

def main(page: ft.Page):
    pygame.init()
    taquin = [1, 2, 3, 4, 5, 6, 7, 8, 0]  # Configuration initiale
    random.shuffle(taquin)  # Mélanger les nombres

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == KEYDOWN:
                direction = event.key
                if direction in [K_z, K_q, K_s, K_d]:
                    move_taquin(taquin, direction)
                    draw_taquin(page, taquin)

        page.wait_for_event()

ft.app(target=main)
