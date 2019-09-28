import pygame

pygame.init()
#Вставить_фоновую_музыку
pygame.mixer.music.load('321.mp3')
pygame.mixer.music.play()


import pygame
#Проверим_столкновение_двух_обьектов
def pell(x1, y1, x2, y2, db1, db2):
    if x1 > x2-db1 and x1 < x2+db2 and y1 > y2-db1 and y1 < y2+db2:
        return 1
    else:
        return 0

pygame.init()
#Зададим_размер_окна
window = pygame.display.set_mode((500, 500))
#Зададим_размер_фона
screen = pygame.Surface((500, 500))
#Размер_нашего_персонажа
player = pygame.Surface((60, 81))
#Размер_нашего_противника
vrag = pygame.Surface((60, 60))
#Размер_нашего_патрона
pull = pygame.Surface((50, 50))
#Изначальное_кол-во_очков
points = 0

player.set_colorkey((0, 0, 0))
vrag.set_colorkey((0, 0, 0))
pull.set_colorkey((0, 0, 0))

img_14 = pygame.image.load('14.png')
img_13 = pygame.image.load('13.png')
img_u = pygame.image.load('u.png')

myfont = pygame.font.SysFont('Helvetica', 20)
#Изначальные_координаты_патрона
a_x = 1000
a_y = 1000

strike = False
#Координаты_нашего_противника
z_x = 0
z_y = 0
#Зададим_координаты_нашему_персонажу
x_p = 180
y_p = 360

right = True

done = False
#Создадим_игровой_цикл
while done == False:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            done = True
#Назначим_кнопкам_действие_персонажем
        if e.type == pygame.KEYDOWN and e.key == pygame.K_s:
            y_p += 13
        if e.type == pygame.KEYDOWN and e.key == pygame.K_w:
            y_p -= 13
        if e.type == pygame.KEYDOWN and e.key == pygame.K_a:
            x_p -= 13
        if e.type == pygame.KEYDOWN and e.key == pygame.K_d:
            x_p += 13
#Назначеним_кнопке_выстрел
        if e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
            if strike == False:
                strike = True
                a_x = x_p - -8
                a_y = y_p - 40

#Зададим_логику_движений_патрону
    if strike:
        a_y -= 0.5
        if a_y < 0:
            strike = False
            a_y = 1000
            a_x = 1000

    if pell(a_x, a_y, z_x, z_y, 20, 40):
        points += 1
        strike = False
        a_y = 1000
        a_x = 1000

#Зададим_логику_движения_противнику
    if right:
        z_x += 0.5
        if z_x > 600:
            z_x -= 0.5
            right = False
    else:
        z_x -= 0.2
        if z_x < 0:
            z_x += 0.2
            right = True

    string = myfont.render('Голов : ' +str(points), 0, (255, 0 ,0))
#Отобразим_на_экране_все_предметы
    screen.fill((0,0,0))
    pull.blit(img_14, (0, 0))
    player.blit(img_13, (0, 0))
    vrag.blit(img_u, (0, 0))
    screen.blit(string, (0, 50))
    screen.blit(pull, (a_x, a_y))
    screen.blit(vrag, (z_x, z_y))
    screen.blit(player, (x_p, y_p))
    window.blit(screen, (0, 0))
    pygame.display.update()

#Выходим_из_игры
pygame.quit()
