'''
(n+1)*3 + 1
n/2
'''

from random import choice
from pygame import draw, display, event, QUIT, MOUSEBUTTONDOWN, mouse, time

FPS = 1000
WIGHT, HEIGTH = 1200, 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
colors = [[255, 255, 255], [255, 0, 0], [0, 255, 0], [0, 0, 255]]
ListPos = []
ListDelta = []
ListBool = []
clock = time.Clock()


def Draw(disp, count, listpos, listdelta, listbool) -> None:
    disp.fill(choice(colors))
    posX = 0; posY = 0;
    for i in range(0, count-1):
        if listpos[i][0] + listdelta[i][0] < 0 or listpos[i][0] + listdelta[i][0] > WIGHT-30:
            listbool[i][0] = not listbool[i][0]
        if listpos[i][1] + listdelta[i][1] < 0 or listpos[i][1] + listdelta[i][1] > HEIGTH-30:
            listbool[i][1] = not listbool[i][1]


        if listbool[i][0]:
            listdelta[i][0] += 1
        else:
            listdelta[i][0] -= 1
        if listbool[i][1]:
            listdelta[i][1] += 1
        else:
            listdelta[i][1] -= 1
        posX = listpos[i][0] + listdelta[i][0]; posY = listpos[i][1] + listdelta[i][1]
        draw.rect(disp, WHITE, (posX, posY, 30, 30))
        display.update(posX, posY, 30, 30)


def window():
    allDots = 1
    sc = display.set_mode((WIGHT, HEIGTH))
    flEx = True
    while flEx:
        for ev in event.get():
            if ev.type == QUIT:
                flEx = False
            if ev.type == MOUSEBUTTONDOWN:
                print(mouse.get_pos())
                ListPos.append(mouse.get_pos())
                ListDelta.append([0, 0])
                ListBool.append([choice([True, False]), choice([True, False])])
                #print(ListPos)
                #print(len(ListPos))
                allDots = allDots + 1

        display.update()
        Draw(sc, allDots, ListPos, ListDelta, ListBool)
        clock.tick(FPS)


window()
print("Die")
print(ListPos)

