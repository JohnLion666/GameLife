import time as TIME
from random import choice, randint
from pygame import display, event, draw, time, QUIT, MOUSEBUTTONDOWN, mouse


FPS = 60000
WIGHT, HEIGTH = 1200, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (60, 60, 60)
colors = [[255, 255, 255], [255, 0, 0], [0, 255, 0], [0, 0, 255]]
clock = time.Clock()
listFirstGen = [[choice([1, 0, 0, 0]) for j in range(int(HEIGTH/10))] for i in range(int(WIGHT/10))]
listNextGen = [[choice([1, 0, 0, 0]) for j in range(int(HEIGTH/10))] for i in range(int(WIGHT/10))]




def author():
    print("""
    ---------------------------------------------------------------
    |                                                             |
    |                         @JohnLion                           |
    |                     telegram - @Fgfgfgsn                    |  
    |                                                             |
    ---------------------------------------------------------------
    """)

def rules():
    TIME.sleep(1)
    print( """
        Место действия этой игры — «вселенная» — это размеченная на клетки поверхность или плоскость
         — безграничная, ограниченная, или замкнутая (в пределе — бесконечная плоскость).
    Каждая клетка на этой поверхности может находиться в двух состояниях: быть «живой» (
    заполненной) или быть «мёртвой» (пустой). Клетка имеет восемь соседей, окружающих её.""")
    TIME.sleep(1)
    print("""
    Распределение живых клеток в начале игры называется первым поколением. Каждое следующее 
    поколение рассчитывается на основе предыдущего по таким правилам:
        в пустой (мёртвой) клетке, рядом с которой ровно три живые клетки, зарождается жизнь;
        если у живой клетки есть две или три живые соседки, то эта клетка продолжает жить; в противном случае, если соседей меньше двух или больше трёх, клетка умирает («от одиночества» или «от перенаселённости»)""")
    TIME.sleep(1)
    print("""
    Игра прекращается, если
        на поле не останется ни одной «живой» клетки
        конфигурация на очередном шаге в точности (без сдвигов и поворотов) повторит себя же на одном из более ранних шагов (складывается периодическая конфигурация)
        при очередном шаге ни одна из клеток не меняет своего состояния (складывается стабильная конфигурация; предыдущее правило, вырожденное до одного шага назад)
    """)
    TIME.sleep(1)

def drawNet(disp, wight, heigth):
    for i in range(0, wight, 10):
        for j in range(0, heigth, 10):
            draw.circle(disp, GRAY, (i, j), 1)
    display.update()
    pass

def drawNPS(disp, x, y):
    if 0 <= x % 10 <= 4:
        posX = x - x % 10
    elif 5 <= x % 10 <= 10:
        posX = x - x % 10 + 10
    if 0 <= y % 10 <= 4:
        posY = y - y % 10
    elif 5 <= y % 10 <= 10:
        posY = y - y % 10 + 10
    draw.rect(disp, WHITE, [posX+1, posY+1, 8, 8])
    display.update(posX, posY, 10, 10)
    pass

def Draw(disp, x, y, color):
    draw.rect(disp, color, [x + 1, y + 1, 8, 8])
    #display.update(x, y, 10, 10)
    pass

def getNeighbors(list, x, y) -> int:
    count = 0
    a1 = x - 1; b1 = y - 1;
    a2 = x + 1; b2 = y + 1;
    #check verge
    if a1 <= 0:
        a1 = len(list)-1
    if b1 <= 0:
        b1 = len(list[0])-1
    if a2 >= len(list)-1-1:
        a2 = 0
    if b2 >= len(list[0])-1:
        b2 = 0
    #counting neighbors
    if list[a1][b1] == 1:
        count += 1
    if list[a1][y] == 1:
        count += 1
    if list[a1][b2] == 1:
        count += 1
    if list[x][b1] == 1:
        count += 1
    if list[x][b2] == 1:
        count += 1
    if list[a2][b1] == 1:
        count += 1
    if list[a2][y] == 1:
        count += 1
    if list[a2][b2] == 1:
        count += 1
    return count

def getNextGen (listfg, minneighbors, maxneighbors, birthNeibors) -> list:
    nextgen = listfg
    for i in range(0, len(nextgen)):
        for j in range(0, len(nextgen[0])):
            if nextgen[i][j] == 0 and getNeighbors(nextgen, i, j) == birthNeibors: #birthday NPS
                nextgen[i][j] = 1
            if nextgen[i][j] == 1 and minneighbors <= getNeighbors(nextgen, i, j) <= maxneighbors: #dead NPS
                continue
            else:
                nextgen[i][j] = 0
    return nextgen

def randomNPS(dicp, listfg):
    #print(listfg)
    #print(len(listfg))
    #print(len(listfg[0]))
    for i in range(0, len(listfg)):
        for j in range(0, len(listfg[0])):
            if listfg[i][j] == 1:
                Draw(dicp, (i+1)*10, (1+j)*10, color=choice(colors))
            else:
                Draw(dicp, (i+1)*10, (1+j)*10, BLACK)
    pass

def window(percent=0, Min=2, Max=3, Birth=3):
    listFirstGen = [[choice([1, 0, 0, 0, 0, 0, 0, 0]) for j in range(int(HEIGTH/10))] for i in range(int(WIGHT/10))]
    listNextGen = [[choice([1, 0, 0, 0, 0, 0, 0, 0]) for j in range(int(HEIGTH/10))] for i in range(int(WIGHT/10))]
    sc = display.set_mode((WIGHT, HEIGTH))
    sc.fill(BLACK)
    Flexxxxxx = True
    drawNet(sc, WIGHT, HEIGTH)
    randomNPS(sc, listFirstGen)
    display.update()
    #TIME.sleep(1)
    while Flexxxxxx:
        for ev in event.get():
            if ev.type == QUIT:
                Flexxxxxx = False
            if ev.type == MOUSEBUTTONDOWN:
                drawNPS(sc, mouse.get_pos()[0], mouse.get_pos()[1])
                listFirstGen[int(mouse.get_pos()[0]/10)][int(mouse.get_pos()[1]/10)] = 1
        listNextGen = getNextGen(listFirstGen, Min, Max, Birth)
        for i in range(0, int((WIGHT*HEIGTH)/100 * percent/100)):
            listNextGen[randint(0, len(listNextGen)-1)][randint(0, len(listNextGen[0])-1)] = 0
        randomNPS(sc, listNextGen)
        display.update()
        TIME.sleep(0.1)
        listFirstGen = listNextGen
    clock.tick(FPS)


author()
rules()
print("Также вы можете внести изменения в игру")
try:
    PERCENT = input("процент рандомной смертности [0 .. 100] >>> ")
    MIN = input("Минимальное кол-во соседей [1..7]>>>")
    MAX = input("Максимальное кол-во соседей [2..8]>>>")
    BIRTH = input("Кол-во 'родителей' [1..8]>>>")
    b = int(input("Are you ready? [1]"))

    if b == 1:
        window(int(PERCENT), int(MIN), int(MAX), int(BIRTH))
    print("die")
except Exception:
    window()
    print("die")