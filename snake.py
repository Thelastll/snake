import pygame
from random import randint
pygame.init()

# основные переменные
W, H = 800, 800
fps = 250
clock = pygame.time.Clock()
black = (0, 0, 0)
white = (255, 255, 255)
font_ = pygame.font.SysFont('calibri', 24)
sc_text = font_.render('GAME OVER', 1, white, black)
pos_text = sc_text.get_rect(center = (400, 400))
pygame.display.set_caption('score 0')
yab_pos_x = randint(0, 39)
yab_pos_y = randint(0, 39)

sc = pygame.display.set_mode((W, H))

speed = 1
x = 20
y = 760
put = 2
put1 = 0
score = 0
wr = 1
wr_ = 1
t = 0

zmeya = [[-20, 760], [-40, 760], [-60, 760], [-80, 760], [-100, 760], [-120, 760], [-140, 760]]

# игровой цикл
while wr:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            wr = 0
            wr_ = 0

# отрисовка тела и яблок
    sc.fill(black)

    if x == yab_pos_x*20 and y == yab_pos_y*20:
        yab_pos_x = randint(0, 39)
        yab_pos_y = randint(0, 39)
        score += 1
        pygame.display.set_caption('score ' + str(score))

        zmeya += [-40, 760],

    pygame.draw.rect(sc, (255, 0, 0),  (yab_pos_x*20, yab_pos_y*20, 20, 20))
    
    for i in range(len(zmeya)):
        sv = len(zmeya)-1-i
        xvost = zmeya[len(zmeya)-1]
        if t % 20 == 0:
            zmeya[len(zmeya)-1-i] = zmeya[len(zmeya)-2-i]
       
        pygame.draw.rect(sc, (255, 255, 255,), (zmeya[sv][0], zmeya[sv][1], 20, 20))
        pygame.draw.rect(sc, (255, 255, 255,), (xvost[0], xvost[1], 20, 20))

        zmeya[0] = [x, y]

# нажатия
    keys = pygame.key.get_pressed()

    if keys[pygame.K_DOWN] and put != 3:
        put1 = 4
    if keys[pygame.K_LEFT] and put != 2:
        put1 = 1
    if keys[pygame.K_RIGHT] and put != 1:
        put1 = 2
    if keys[pygame.K_UP] and put != 4:
        put1 = 3

    if t % 20 == 0:
        if put1 == 4:
            put = 4
        if put1 == 1:
            put = 1
        if put1 == 2:
            put = 2
        if put1 == 3:
            put = 3


    if put == 1:
        x -= speed
    elif put == 2:
        x += speed
    if put == 3:
        y -= speed
    elif put == 4:
        y += speed

    xvost[0] += (zmeya[len(zmeya)-2][0]-zmeya[len(zmeya)-1][0])/20
    xvost[1] += (zmeya[len(zmeya)-2][1]-zmeya[len(zmeya)-1][1])/20

# отрисовка головы
    pygame.draw.rect(sc, (130, 255, 255,), (x, y, 20, 20))

# столкновения
    if x < 0 or x > 780:
        wr = 0
    if y < 0 or y > 780:
        wr = 0  

    for i in zmeya:
        if x == i[0] and y == i[1]:
            wr = 0
    
    t += 1

    pygame.display.update()
    clock.tick(fps)

# game over
for i in range(80):
    sc.fill(black)
    font_ = pygame.font.SysFont('calibri', i)
    sc_text = font_.render('GAME OVER', 1, white, None)
    pos_text = sc_text.get_rect(center = (400, 400))
    sc.blit(sc_text, pos_text)
    pygame.display.update()
    clock.tick(150)

while wr_:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            wr_ = 0
    
    sc.fill(black)
    sc.blit(sc_text, pos_text)

    pygame.display.update()
    clock.tick(fps)